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



    print(mean)
    print(variance)
    print(normal_distribution(mean,variance,data_array[0]))

normal_trend('diff_data.txt')


