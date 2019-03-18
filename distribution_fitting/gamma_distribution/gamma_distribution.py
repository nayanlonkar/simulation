import math
from main import *

def mean_funct(data_array):
    mean = sum(data_array)/len(data_array)
    return mean 

#This function will give theta parameter
def theta_funct(data_array):
    theta = 1/mean_funct(data_array)
    return theta

#This function will give 1/M. By using this we can predict the value of beta parameter
def oneByM(data_array):
    temp1 = math.log(mean_funct(data_array))              #this will return =  ln(mean)
    log_data_array = [math.log(i) for i in data_array]
    temp2  = sum(log_data_array)/len(log_data_array)
    temp3 = temp1 - temp2 
    return 1/temp3

#probability density function of gamma function
def gamma_pdf(theta, beta, x_val):
    temp1 = (theta * beta)/math.gamma(beta)
    temp2 = (theta * beta * x_val)**(beta - 1)
    temp3 = math.exp(-1 * theta * beta * x_val)
    return (temp1 * temp2 * temp3)

def gamma_distribution(filename):
    data_array = readfile(filename)
    #data_array = [70.292,10.107,48.386,20.480,13.053,25.292,14.713,39.166,17.421,13.905,30.215,17.137,44.024,10.552,37.298,16.314,28.073,39.019,32.330,36.547]
    noOfIntervals = 15
    intervalSize = (max(data_array) - min(data_array))/noOfIntervals  
    theta = theta_funct(data_array)
    print(f"theta is : {theta}")
    print(f"1/M value is : {oneByM(data_array)} ")
    beta = float(input("Enter the beta parameter from table A.9 based on 1/M value : "))

    temp = min(data_array)
    temp_list = [temp]
    for i in range(noOfIntervals):
        temp += intervalSize
        temp_list.append(temp)
    #interval list
    interval_list = [[temp_list[i], temp_list[i+1]] for i in range(len(temp_list)-1)]
    #actual frequency list
    frequency_list = frequency_count(data_array, interval_list)

    #expected frequency calculation
    expected_pro = []
    for i in interval_list:
        a = i[0]
        b = i[1]
        n = 100
        h = (b - a)/n 
        sum1 = 0
        for j in range(1, n-1):
            sum2 = gamma_pdf(theta, beta, (a+j*h))
            sum1 += sum2
        sum1 = sum1 * 2
        sum1 = sum1 + gamma_pdf(theta, beta, a) + gamma_pdf(theta, beta, b)
        sum1 = sum1 * (h/2)
        expected_pro.append(sum1)
    #to calculate expected frequency, multiply expected probability by sample size
    expected_frequency = [len(data_array) * i for i in expected_pro]
    
    #chiSquare test
    chiSquare_array = []
    for i in range(len(frequency_list)):
        temp = (frequency_list[i] - expected_frequency[i]) ** 2
        temp = temp / expected_frequency[i]
        chiSquare_array.append(temp)
    chiSquare_value = sum(chiSquare_array)
    print(f"ChiSquare value is : {chiSquare_value}")

gamma_distribution('gamma.txt')
