import requests
import xmltodict
import math
from flask import Flask, request

app = Flask(__name__)

def get_data() -> dict:
    """Gather data from ISS website

    Gather XML file from the ISS website and converts it into a dicitionary

    Args:
       None

    Returns:
        Dictionary with entire dataset.
    """    

    url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
    response = requests.get(url)
    data = xmltodict.parse(response.text)
    type(data)
    return data

@app.route('/', methods = ['GET'])#returns the entire data set
def get_data_set() -> dict:
    """Return entire data set from ISS Website

    Takes in request using flask to return entire set. 

    Args:
       None

    Returns:
        Dictionary with entire dataset.
    """
    data = get_data()
    return data
    

@app.route('/epochs', methods = ['GET'])#A list of all Epochs in the data set
def get_epoch_list() -> list:
    """Return list of all Epochs in the data set

    Takes in request using flask and returns a list of all the epochs in the dataset.

    Args:
       None

    Returns:
        List of all the epochs
    """
    data = get_data()
    epochs = data['ndm']['oem']['body']['segment']['data']['stateVector']
    return epochs


@app.route('/epochs/<int:epoch>', methods = ['GET'])#State vectors for a specific Epoch from the data set
def get_each_vectors(epoch:int) -> dict:
    """Return specific epoch

    Takes in request using flask and returns specific epoch in the list.

    Args:
       Takes in an integer that is the ith epoch in the list

    Returns:
        Dictionary with all of the data related to that epoch
    """
    data = get_data()
    epochs = data['ndm']['oem']['body']['segment']['data']['stateVector']
    return epochs[int(epoch)]


@app.route('/epochs/<int:epoch>/speed', methods = ['GET'])#Instantaneous speed for a specific Epoch in the data set (math required!)
def get_instantaneous_speed(epoch:int) -> str:
    """Return Epoch's speed

    Based on requested epoch number calculate and return its velocity.

    Args:
       Takes in an integer that is the ith epoch in the list

    Returns:
        Dictionary containing the velocity of the epoch
    """
    data = get_data()
    epochs = data['ndm']['oem']['body']['segment']['data']['stateVector']
    i = int (epoch)
    x_velocity = float(epochs[i]['X_DOT']['#text'])
    y_velocity = float(epochs[i]['Y_DOT']['#text'])
    z_velocity = float(epochs[i]['Z_DOT']['#text'])
    velocity = math.sqrt((x_velocity ** 2) + (y_velocity ** 2) + (z_velocity ** 2))
    return {'Velocity':velocity}

# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
