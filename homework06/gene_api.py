from flask import Flask, request
import requests
import json
import redis

app = Flask(__name__)

global gene_data
url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json'

def get_redis_client():
    return redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses = True) #decode_response turn byte key into a string we can use

rd = get_redis_client()

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def handle_data():
    global data
    if request.method == 'POST':
        response = requests.get(url)
        gene_data = response.json()['response']['docs']
        for item in gene_data:
            rd.set(item.get('hgnc_id'), json.dumps(item))
            
        return "Data was loaded in"

    
    elif request.method == 'GET':
        output_list = []
        for item in rd.keys():
            output_list.append(rd.hgetall(item))
        return output_list
    
         #for item in rd:
            #gene = json.loads(rd.get(f'HGNC:5'))
            
            #return gene
    elif request.method == 'DELETE':
        rd.flushdb()
        return f'data deleted, tehre are {rd.keys()} keys in the db\n'
    else:
        return 'the method you tried does not work\n'





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    
