from main import *
import math

#lamda is the inverse of the mean of the data(i.e 1/mean)
def lamda_fun(data_array):
    mean = sum(data_array)/len(data_array)
    return (1/mean)    

def exponential_function(lamda, x_val):
    temp = lamda * (math.exp(-lamda * x_val))
    return temp

def exponential_distribution(filename):
    data_array = readfile(filename)
    noOfInterval = 15
    intervalSize = (max(data_array) - min(data_array))/noOfInterval 
    
    temp = min(data_array)
    temp_list = [temp]
    for i in range(noOfInterval):
        temp += intervalSize 
        temp_list.append(temp)

    #for upper and lower limits to be infinity
    #interval list creation
    interval_list = [[temp_list[i], temp_list[i+1]] for i in range(len(temp_list)-1)]
    #actual frequency list
    frequency_list = frequency_count(data_array, interval_list)
    lamda = lamda_fun(data_array)
    #expected frequency calculation
    expected_prob = []
    for i in interval_list:
        a = i[0]
        b = i[1]
        n = 100         #no of intervals
        h = (b - a)/n
        sum1 = 0
        for j in range(1,n-1):
            sum2 = exponential_function(lamda, (a+j*h))
            sum1 += sum2
        sum1 = sum1 * 2
        sum1 = sum1 + exponential_function(lamda, a) + exponential_function(lamda, b)
        sum1 = sum1 * (h/2)
        expected_prob.append(sum1) 
    #to calculate expected frequency multiply expected probability by sample size
    expected_frequency = [len(data_array) * i for i in expected_prob]  
    #chiSquare test
    chiSquare_array = []
    for i in range(len(frequency_list)):
        temp = (frequency_list[i] - expected_frequency[i]) ** 2
        temp = temp / expected_frequency[i]
        chiSquare_array.append(temp)
    chiSquare_value = sum(chiSquare_array)
    print('ChiSquare value is : ',chiSquare_value)            
            
exponential_distribution('exponential.txt')


    
