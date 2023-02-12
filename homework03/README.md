# Analyzing Mars Water Quality


## Folder Contents / Project Objective

This directory contains one python script called analyze_water that analyzes the turbidity of the water of the five most recent water samples. It is collecting the data from a json file that is continously updating with new samples. The second script is called test_analyze_water that has test that check that the math within analyze_water script are functioning properly. 

## Accessing data set from the original source

The data is a dictionary with the keywords 'datetime', 'sample_volume', 'calibration constant', 'detector_current', and 'analyzed by'. The json formatted data can be found at this link: https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

## Description of python scripts (1-2 sentences)

### analyze_water

Imports request which is needed for getting json file from the internet, which it then uses to get the data needed for the two functions. Contains two functions, one to calculate turbidity and the other to calcualte the time needed for it to reach turbidity level of 1 NTU.

### test_analyze_water

Contains two functions that are automated to run with pytest, which check that the functions are returning appropriate results. The functions name begin with test_ followed by the name of the function which  they are testing.  


Request library and pytest need to be installed to run the code, which can be installed with the lines of code below.

```
pip3 install --user requests

pip3 install --user pytest

```
To run the analyze_water script simply run the command
```
python3 analyze_water.py
```
The first line of the output shows the current tubidity levels in NTU units, the second line displays if it is at a safe level (below 1 NTU), and the third line displays how long it will take for the sample to reach below 1 NTU.

```
Average turbidity based on most recent five measurements = 65.1206 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 207 hours
```
To run the test simply type pytest into the terminal.
