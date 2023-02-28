# International Space Station Data 

## Purpose

The purpose of this project is to make working with and looking at the International Space Station data much easier. The project uses recent and publicly available data that allows the user to be able to see the ISS position and velocities. Within this repository there is a dockerfile (Dockerfile) that containerizes the flask app. There is also the flask app (iss_tracker.py), which creates a framework where the user is able to send request and the server will return an appropriate response.

## ISS Data 

The data can be downloaded from this link: https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml
The data, however, is gathered through the python script from the link using the request library. The data is an XML file containing epochs with their respective position (x,y,z) and their velocity (x,y,z). The units are respectively km and km/s. While this is the information we are interested, the XML file also contains metadata and more. 

## Flask app

Flask is a Python library and framework for building web servers. This is used to create a server where the user can make request and the server will return an appropriate resonse.   

## Running the app thorugh Docker

Before running the app you need to pull the Docker image from DockerHub:

```
$docker pull antjim19037/iss_tracker:hw05
```

We will then build the image:

```
$docker build -t antjim19037/iss_tracker:hw05 .
```

We will now run the Docker image:

```
$docker run -it --rm -p 5000:5000 antjim19037/iss_tracker:hw05
```
The -p flag takes the form <host port>:<container port> and connects the two ports. The Flask app is now running. You should see the ports which are being used. These ports can be used to make request:
```
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
```

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
