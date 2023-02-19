# International Space Station Speed Tracker

## Purpose

This directory contains a README and the iss_tracker python script. The purpose of this project is to be able to calculate and look at data from the ISS at specific times. 

## ISS Data 

The data can be downloaded from this link: https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml
The data, however, is gathered through the python script from the link using the request library. The data is an XML file containing epochs with their respective position (x,y,z) and their velocity (x,y,z).

## Flask app

The flask app takes in a request from the client which the framework then returns a string. 

## Running the app

Before running the app ensure you have installed the appropriate libraries.
```
$pip3 install --user requests
$pip3 install --user xmltodict
```
In one terminal you will be running the app. Ensure that you are in the same directory as the python script iss_tracker.py. In the terminal run the code below:
```
$ flask --app iss_tracker.py --debug run
```
In another terminal you can type one of the four routes "/" , "/epochs" , "/epochs/<int:epoch>" , and"/epochs/<int:epoch>/speed"
```
$curl localhost:5000/
$curl localhost:5000/epochs
$curl localhost:5000/epochs/<int:epoch> 
$curl localhost:5000/epochs/<int:epoch>/speed
```
## Output
The first route ("/") will result in the entire dataset being returned. You will see all of the information wihtin the XML file as a dictionary. The end of your output will look like: 
```
   },
          "metadata": {
            "CENTER_NAME": "EARTH",
            "OBJECT_ID": "1998-067-A",
            "OBJECT_NAME": "ISS",
            "REF_FRAME": "EME2000",
            "START_TIME": "2023-048T12:00:00.000Z",
            "STOP_TIME": "2023-063T12:00:00.000Z",
            "TIME_SYSTEM": "UTC"
          }
        }
      },
      "header": {
        "CREATION_DATE": "2023-049T01:38:49.191Z",
        "ORIGINATOR": "JSC"
      }
    }
  }
}
```
The second route (/epochs) will result in a list of epochs being returned. Within this output you will see all of the information relating to each epoch. The end of your output will look like: 
```
 {
    "EPOCH": "2023-063T12:00:00.000Z",
    "X": {
      "#text": "2820.04422055639",
      "@units": "km"
    },
    "X_DOT": {
      "#text": "5.0375825820999403",
      "@units": "km/s"
    },
    "Y": {
      "#text": "-5957.89709645725",
      "@units": "km"
    },
    "Y_DOT": {
      "#text": "0.78494316057540003",
      "@units": "km/s"
    },
    "Z": {
      "#text": "1652.0698653803699",
      "@units": "km"
    },
    "Z_DOT": {
      "#text": "-5.7191913150960803",
      "@units": "km/s"
    }
  }
]
```
The third route (/epochs/<int:epoch>) will return the information from the epoch requested based on the integer that the route has. Within the information you will find the time of the epoch as well as its x,y,z positions and x,y,z velocity. The output will look like:
```
{
  "EPOCH": "2023-048T12:04:00.000Z",
  "X": {
    "#text": "-5998.4652356788401",
    "@units": "km"
  },
  "X_DOT": {
    "#text": "-2.8799691318087701",
    "@units": "km/s"
  },
  "Y": {
    "#text": "391.26194859011099",
    "@units": "km"
  },
  "Y_DOT": {
    "#text": "-5.2020406581448801",
    "@units": "km/s"
  },
  "Z": {
    "#text": "-3164.26047476555",
    "@units": "km"
  },
  "Z_DOT": {
    "#text": "4.8323394499086101",
    "@units": "km/s"
  }
}
```
The fourth route (/epochs/<int:epoch>/speed) will return the velocity of the epoch requested in the route as a dictionary. The result will be the scalar value of the velocity on km/s. The result will look like:
```
{
  "Velocity": 7.662046317290625
}
```
