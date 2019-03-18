from main import *
import math

def mu_sd(data_array):
    #this function will take data array and will return a tuple containing a mu(mean) and variance
    log_data_array = list(map(math.log,data_array))
    mu = sum(log_data_array)/len(data_array)
    temp_array = [((i - mu)**2) for i in log_data_array]
    sd = sum(temp_array)/len(temp_array)
    return (mu,sd)

def log_normal(mu,sd,x_val):
    if (x_val <= 0):
        return 0
    else:
        temp1 = 1/(math.sqrt(2*(math.pi)*sd)*x_val)
        temp2 = 1/math.exp(((math.log(x_val)-mu)**2)/(2*sd))
        temp3 = temp1 * temp2
    return temp3

def log_trend():
    data_array = readfile('log_normal.txt')
    noIntervals = 15
    intervalSize = (max(data_array) - min(data_array))/noIntervals
    temp_list = [min(data_array)]
    temp = min(data_array)
    for i in range(0,noIntervals):
        temp += intervalSize
        temp_list.append(temp)
    #print(temp_list)
    interval_list = [[temp_list[i],temp_list[i+1]] for i in range(len(temp_list)-1)]
    #print(interval_list)
    frequency_list = frequency_count(data_array,interval_list)
    (mu,sd) = mu_sd(data_array)

    expected_prob = []
    for i in interval_list:
        a = i[0]
        b = i[1]
        h = (b - a)/100
        n = 100
        sum1 = 0
        for j in range(1,99):
            sum2 = log_normal(mu,sd,(a+j*h))
            sum1 = sum1 + sum2
        sum1 = sum1 * 2
        sum1 = sum1 + log_normal(mu,sd,a) + log_normal(mu,sd,b)
        sum1 = sum1/200
        sum1 = sum1 * (b - a)
        expected_prob.append(sum1)
    expected_freq = [100 * i for i in expected_prob]         #to calculate expected frequency multiply probability by sample size
    chiTest_array = []
    for i in range(len(frequency_list)):
        temp = (frequency_list[i] - expected_freq[i]) ** 2
        temp = temp / expected_freq[i]
        chiTest_array.append(temp)
    chiSquare_value = sum(chiTest_array)
    #value of chiSquare
    print(chiSquare_value)

log_trend()

