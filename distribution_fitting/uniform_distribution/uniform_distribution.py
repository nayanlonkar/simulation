from main import *
import math

def uniform_distribution(filename):
    data_array = readfile(filename)
    noOfIntervals = 10
    intervalSize = (max(data_array) - min(data_array))/noOfIntervals

    temp = min(data_array)
    temp_list = [temp]
    for i in range(noOfIntervals):
        temp += intervalSize
        temp_list.append(temp)
    temp_list[len(temp_list) - 1] += 1
    interval_list = [[temp_list[i], temp_list[i+1]] for i in range(len(temp_list)-1)]
    frequency_array = frequency_count(data_array, interval_list)
    
    expectedValue = len(data_array)/noOfIntervals
    
    #chiSquare value
    chiSquare_array = []
    for i in range(len(frequency_array)):
        temp = (frequency_array[i] - expectedValue) ** 2
        temp = temp/expectedValue
        chiSquare_array.append(temp)
    chiSquareValue = sum(chiSquare_array)

    print(f"Chi-Square value is : {chiSquareValue}")
    
uniform_distribution('uniform.txt')


