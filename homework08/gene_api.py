from flask import Flask, request
import requests
import json
import redis
import os
import matplotlin.pyplot as plt
import numpy as np

app = Flask(__name__)

global gene_data
url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json'



def get_redis_client():
    """Connect flask applicaton to redis
    Args: 
       None
    Returns:
       redis client
    """
    redis_ip = os.environ.get('REDIS_IP')
    if not redis_ip:
        raise Exception()
    rd = redis.Redis(host=redis_ip,port=6379,db0,decode_responses = True)
    rd2 = redis.Redis(host=redis_ip,port=6379,db1,decode_responses = True)
    return rd,rd2

rd = get_redis_client()

@app.route('/image', methods=['GET','POST', 'DELETE'])
def handle_image():
    global gene_data
    if request.method == 'POST':
        x = np.linspace(0, 2*np.pi, 50)
        plt.plot(x, np.sin(x))
        plt.savefig('my_sinwave.png')
        rd2.set('plot', plt)
        return "Plot has been created"
    elif request.method == "GET":
        return "Image"
    elif request.method == "DELETE":
        rd2.flushdb()
        return "Plot has been delete"

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

    
