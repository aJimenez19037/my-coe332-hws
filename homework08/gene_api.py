from flask import Flask, request, send_file
import requests
import json
import redis
import os
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

global gene_data
url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json'

def get_redis_client(db_val:int):
    """Connect flask applicaton to redis
    Args: 
       None
    Returns:
       None
    """
    redis_ip = os.environ.get('REDIS_IP')
    if not redis_ip:
        raise Exception()
    return redis.Redis(host=redis_ip, port=6379, db=db_val, decode_responses = True) #decode_response turn byte key into a string we can use

rd = get_redis_client(0)
rd2 = get_redis_client(1)

@app.route('/image', methods=['GET', 'POST', 'DELETE'])
def handle_image():
"""Either gets, post, or deletes entire plot

    Args:
       None
    Returns:
       [GET] String: Message informing that the plot has been shared
             png: Plot about approved gene dates. 
       [POST] String: Message informing that plot was loaded into redis
       [DELETE] String: Message infomring that plot was deleted

"""
    global gene_data
    pre_1990 = 0
    pre_2000 = 0
    pre_2010 = 0
    post_2011 = 0
    if request.method == 'POST':
        if len(rd.keys) == 0:
            return "Data has not been loaded in"
        for item in rd.keys():
            item = json.loads(rd.get(item))
            date = item['date_approved_reserved']
            year = int(date[:4])
            if year<=1990:
                pre_1990 = pre_1990+1
            elif year <=2000 and year>1990:
                pre_2000 = pre_2000+1
            elif year <=2010 and year>2000:
                pre_2010 = pre_2010 + 1
            elif year>=2011:
                post_2011 = post_2011 + 1
        year_labels = ['pre_1990','pre_2000','pre_2010','pre_2011']
        val = [pre_1990,pre_2000,pre_2010,pre_2011]
        plt.figure()
        plt.pie(val,labels=year_labels)
        plt.title("Gene Date Appoved")
        plt.savefig('./plot.png')
        with open('./plot.png', 'rb') as f:
            img_bytes = f.read()
        rd2.set('plot', img_bytes)
        return "Plot stored in database"
    elif request.method == 'GET':
        if rd2.exists('plot'):
            img_path = './plot.png'
            with open(img_path, 'wb') as f:
                f.write(rd2.get('plot'))
            return send_file(path,mimetype='plot/png', as_attachment=True)
        return "Image has been returned"
    elif request.method == 'DELETE':
        rd2.flushdb()
        return "Plot has been deleted"
    else:
        return 'the method you tried does not exist\n'
@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def handle_data():
    """Either loads, post, or deletes entire database

    Args:
       None
    Returns: 
       [GET] List: Entire database
       [POST] String: Message informing that data was loaded in
       [DELETE] String: Message infomring that data was deleted

    """
    global gene_data
    if request.method == 'POST':
        response = requests.get(url)
        gene_data = response.json()
        for item in gene_data['response']['docs']:
            key = f'{item["hgnc_id"]}'
            item = json.dumps(item)
            rd.set(key,item)
        return "Data was loaded in \n"
    elif request.method == 'GET':
        output_list = []
        for item in rd.keys():
            output_list.append(json.loads(rd.get(item)))
        return output_list
    elif request.method == 'DELETE':
        rd.flushdb()
        return f'data deleted, there are {rd.keys()} keys in the db\n'
    else:
        return 'the method you tried does not exist\n'

@app.route('/genes',methods=['GET'])
def get_genes() -> list:
    """Return a list of all of the genes within the database
    
    Args:
       None
    Returns:
       List: All of the genes within the database that are stores in redis keys
    """
    return rd.keys()

@app.route('/genes/<string:hgnc_id>', methods=['GET'])
def get_specific_gene(hgnc_id:str) -> dict:
    """Returns a dict with all of the data associated with the specific gene.
    Args: 
       String: Gene of interest.
       Ex: HGNC:5
    Returns: 
       Dictionary: Data related to gene of interest.
    """
    try: 
        a = json.loads(rd.get(hgnc_id))
    except TypeError:
        return "HGNC you are searching for does not exist \n"
    data = json.loads(rd.get(hgnc_id))
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    
