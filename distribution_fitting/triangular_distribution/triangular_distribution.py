from main import *
from statistics import mode

#triangular distribution pdf
def triangular_pdf(data_array, x_val):
    a = min(data_array)     #lower limit
    c = max(data_array)     #upper limit
    b = mode(data_array)    #b is mode here
    if (a <= x_val) and (x_val <= b):
        temp1 = 2 * (x_val - a)/(b - a)
        temp1 = temp1/(c - a)
        return temp1
    elif (b < x_val) and (x_val <= c):
        temp1 = 2 * (c - x_val)/(c - b)
        temp1 = temp1/(c - a)
        return temp1
    else:
        return 0
    

def triangular_distribution(filename):
    data_array = readfile(filename)
    noOfIntervals = 9
    intervalSize = (max(data_array) - min(data_array))/noOfIntervals
    temp = min(data_array)
    temp_list = [temp]
    for i in range(noOfIntervals):
        temp += intervalSize
        temp_list.append(temp)
    
    #interval list creation
    interval_list = [[temp_list[i], temp_list[i+1]] for i in range(len(temp_list)-1)]
    temp_interval_list = interval_list
    temp_interval_list[len(temp_interval_list)-1][1] += 1
    
    #actual frequency list
    frequency_list = frequency_count(data_array, interval_list)
    
    #expected frequency calculation
    expected_prob = []
    for i in interval_list:
        a = i[0]
        b = i[1]
        n = 100
        h = (b - a)/n
        sum1 = 0
        for j in range(1,n-1):
            sum2 = triangular_pdf(data_array, (a+j*h))
            sum1 = sum1 + sum2
        sum1 =  sum1 * 2
        sum1 = sum1 + triangular_pdf(data_array, a) + triangular_pdf(data_array, b)
        sum1 = sum1 * (h/2)
        expected_prob.append(sum1)

    #to calculate expected frequency, multiply probability by sample size
    expected_frequency = [len(data_array) * i for i in expected_prob]
    
    #chiSquare test
    chiSquare_array = []
    for i in range(len(frequency_list)):
        temp = (frequency_list[i] - expected_frequency[i]) ** 2
        temp = temp / expected_frequency[i]
        chiSquare_array.append(temp)
    chiSquare_value = sum(chiSquare_array)
    print(f"chiSquare value is : {chiSquare_value}")


triangular_distribution('triangular.txt')
