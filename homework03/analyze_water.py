import json
import requests

def calculate_turbidity(a0,I90):
    I90 = ((I90*180)/3.1415926)
    T = round (a0 * I90, 3)
    #T = Turbidity in NTU Units (0 - 40)
    #a0 = Calibration constant
    #I90 = Ninety degree detector current
#    print("Turbidity: " +str(T))
    return T
    
def calculate_minimum_time(T0):
    b = 0
    d = .02
    Ts = 1
    if (T0 <= 1):
        return 0
    while (float(Ts) < (T0*((1-d)**b))):
        b = b+1
    return b
    
 #   Ts > T0(1-d)**b
   # Ts = Turbidity threshold for safe water
   # T0 = Current turbidity
    #d = decay factor per hour, expressed as a decimal
    #b = hours elapsed
    
def main():
    response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    data = response.json()
    turbidity_total = 0
    for i in range(len(data['turbidity_data'])-5,len(data['turbidity_data'])):
            turbidity_total = turbidity_total + calculate_turbidity(data['turbidity_data'][i]["calibration_constant"], data['turbidity_data'][i]["detector_current"])
            #print (data['turbidity_data'][i]['datetime'])#check that it was the 5 most recent samples

    average_turbidity = turbidity_total/5
    print ( 'Average turbidity based on most recent five measurements = ' + str (average_turbidity) + ' NTU')
    if (average_turbidity > 1):
        print ('Warning: Turbidity is above threshold for safe use')
        minimum_time = calculate_minimum_time(average_turbidity)
        print('Minimum time required to return below a safe threshold = ' + str(minimum_time) + ' hours')
    else:
        print('Info: Turbidity is below threshold for safe use')
        print('Minimum time required to return below a safe threshold = 0 hours')

    



if __name__ == '__main__':
        main()
