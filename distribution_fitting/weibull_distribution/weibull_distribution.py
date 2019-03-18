#this file contains program to fit weibull distribution. 
#This is a weibull distribution with two parameters alpha(scale parameter) and beta(shape parameter). 
#Location parameter is considered as zero.
from main import *
import math
from weibull_parameter_estimation import *

#weibull probability density function
def weibull_pdf(alpha, beta, x_val):
    if x_val < 0 :
        return 0
    else:
        temp1 = (beta/alpha) * ((x_val/alpha)**(beta-1))
        temp2 = math.exp(-1 * ((x_val/alpha)**beta))
        return temp1 * temp2 

def weibull_distribution(filename):
    data_array = readfile(filename)
    noOfIntervals = 15
    intervalSize = (max(data_array) - min(data_array))/noOfIntervals

    temp = min(data_array)
    temp_list = [temp]
    for i in range(noOfIntervals):
        temp += intervalSize
        temp_list.append(temp)
    #interval list
    interval_list = [[temp_list[i], temp_list[i+1]] for i in range(len(temp_list)-1)]
    #observed frequency list
    frequency_list = frequency_count(data_array, interval_list)
    alpha = alpha_estimation(data_array)
    beta = beta_estimation(data_array)

    #expected frequency calculations
    expected_pro = []
    for i in interval_list:
        a = i[0]
        b = i[1]
        n = 100
        h = (b - a)/n
        sum1 = 0
        for j in range(1, n-1):
            sum2 = weibull_pdf(alpha, beta, (a+j*h))
            sum1 += sum2
        sum1 = sum1 * 2
        sum1 = sum1 + weibull_pdf(alpha, beta, a) + weibull_pdf(alpha, beta, b)
        sum1 = sum1 * (h/2)
        expected_pro.append(sum1)
    #to calculate expected frequency, multiply expected probability by sample size
    expected_frequency = [len(data_array)* i for i in expected_pro]
    
    #chiSquare test
    chiSquare_array = []
    for i in range(len(frequency_list)):
        temp = (frequency_list[i] - expected_frequency[i]) ** 2
        temp = temp/expected_frequency[i]
        chiSquare_array.append(temp)
    chiSquareValue = sum(chiSquare_array)
    print(f"chiSquare value is: {chiSquareValue}")


weibull_distribution('weibull.txt')
