
# Analyzing hypothetical Mars robot explorer 

This project was created to test the usage of JSON files. Not only for writing data regarding meteors on mars, but also to test reading the data from a JSON file. When scaled up we are able to determine the length of the mission for a robot traveling at 10km/h.

## Python scripts descriptions

***generate_sites.py*** is a python script that generates data for 5 meteorites, which includes latitude (between 16-18), longitude (between 82-84), and composition (stony, iron, stony-iron).This data is then assembled into a dictionary with one key 'sites'.

***calculate_trip.py*** is a python script that calculates the total expected time to the robot to travel and take samples from the five meteors. This path is not optimized, and time sampled varies depending on the composition of the meteor.

## Compiling the code

To run the code simply type into the terminal:


```bash
python3 generate_site.py

or

python3 calculate_trip.py
```


## Analyzing Output

For the scipt generate_sites.py there will be no output, as the script only creates a JSON file. To see the data created simply open the file with your favorite text editor. Ex:

```bash
emacs meteorites.json
```

The output of the scirpt calculate_trip shows the time to travel from the robots current position to the next meteorite followed by the time it will take to take to sample the meteorite. At the end of the output it will show the number of legs (meteorites sampled) and the total time it will take to complete its mission. 

