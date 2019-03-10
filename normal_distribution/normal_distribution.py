from main import *
import math

def mean_variance(data_array):
    mean = sum(data_array)/len(data_array)
    temp_array = [(data_array[i] - mean)**2 for i in range(len(data_array))]
    variance = sum(temp_array)/len(temp_array)
    return (mean,variance)
    
def normal_distribution(mean,variance,x_val):
    temp1 = 1/math.sqrt(variance*2*math.pi)
    temp2 = ((x_val - mean)**2)/variance
    temp2 = (-1/2) * temp2
    temp2 = math.exp(temp2)
    temp = temp1 * temp2
    return temp 


def normal_trend(filename):
    data_array = readfile(filename)
    noOfInterval = 15
    intervalSize = (max(data_array) - min(data_array))/noOfInterval 
    (mean, variance) = mean_variance(data_array)
    
    temp = min(data_array)
    temp_list = [temp]
    for i in range(noOfInterval):
        temp += intervalSize 
        temp_list.append(temp)

    #for upper and lower limits to be infinity
    temp_list[0] = temp_list[0] - 100
    temp_list[len(temp_list)-1] = temp_list[len(temp_list)-1] + 100
    #interval list creation
    interval_list = [[temp_list[i], temp_list[i+1]] for i in range(len(temp_list)-1)]
    #actual frequency list
    frequency_list = frequency_count(data_array, interval_list)

    #expected frequency calculation
    expected_prob = []
    for i in interval_list:
        a = i[0]
        b = i[1]
        n = 100         #no of intervals
        h = (b - a)/n
        sum1 = 0
        for j in range(1,n-1):
            sum2 = normal_distribution(mean, variance, (a+j*h))
            sum1 += sum2
        sum1 = sum1 * 2
        sum1 = sum1 + normal_distribution(mean,variance,a) + normal_distribution(mean,variance,b)
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
    print(f"chiSquare value is :{chiSquare_value}")            
            
normal_trend('normal.txt')
