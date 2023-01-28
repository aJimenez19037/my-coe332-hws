#!/usr/bin/env python3

import json
import math

mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
            lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
            d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
            return ( mars_radius * d_sigma )


with open('meteorites.json', 'r') as f:
            ml_data = json.load(f)
            robotLatitude = 16
            robotLongitude = 82
            timeTotal = 0
            for i in range(len(ml_data['sites'])):
                        distance = calc_gcd(robotLatitude, robotLongitude, ml_data["sites"][i]["latitude"],ml_data["sites"][i]["longitude"])
                        timeToTravel = distance/10.0 #10km/h
                        if (ml_data['sites'][i]['composition'] == 'stony'):
                                    timeToSample = 1
                        elif (ml_data['sites'][i]['composition'] == 'iron'):
                                    timeToSample = 2
                        else:
                                    timeToSample = 3
                        #print ("{:.2f}".format(timeToTravel))
                        print ('leg = ' + str(i+1) + ', time to travel = ' + "{:.2f}".format(timeToTravel) + " hr, time to sample = " + "{:.2f}".format(timeToSample) + " hr") 
                        timeTotal = timeToTravel + timeToSample + timeTotal
            print ("==========================")
            print ("number of legs = " + str(len(ml_data['sites'])) + ", total time elapsed = " + "{:.2f}".format(timeTotal) + " hr")
