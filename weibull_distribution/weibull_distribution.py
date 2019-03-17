from main import *
import math

#equation 9.12
def funct1(beta, data_array):
    n = len(data_array)
    log_data_array = [math.log(i) for i in data_array]
    beta_data_array = [i**beta for i in data_array]
    temp1 = 0
    for i in range(n):
        temp2 = beta_data_array[i] * log_data_array[i]
        temp1 += temp2
    temp1 = (n * temp1)/sum(beta_data_array)
    result = (n/beta) * sum(log_data_array) - temp1
    return result

#equation 9.13
#derivative of equation 9.12
def funct2(beta, data_array):
    n = len(data_array)
    log_data_array = [math.log(i) for i in data_array]
    beta_data_array = [i**beta for i in data_array]

    temp1 = 0
    for i in range(n):
        temp2 = beta_data_array[i] * (log_data_array[i] ** 2)
        temp1 += temp2
    temp1 = (n * temp1)/sum(beta_data_array)

    temp3 = 0
    for i in range(n):
        temp4 = beta_data_array[i] * log_data_array[i]
        temp3 += temp4
    temp3 = n * (temp3 ** 2)
    temp3 = temp3 / (sum(beta_data_array) ** 2)

    result = (-n/beta) - temp1 + temp3
    return result

def mean_funct(data_array):
    result = sum(data_array)/len(data_array)
    return result

#this function calculates the variance
#calculating square root will give standard deviation
def variance_funct(data_array):
    mean = mean_funct(data_array)
    n = len(data_array)
    squared_data_array = [i**2 for i in data_array]
    result = (sum(squared_data_array) - n * (mean ** 2)) / (n-1)
    return result

#this function will determine the value of the beta
def beta_estimation(data_array):
    mean = mean_funct(data_array)
    variance = variance_funct(data_array)
    beta = mean/math.sqrt(variance)
    print(variance)
    print(math.sqrt(variance))
    print(beta,funct1(beta,data_array))
    while(funct1(beta, data_array) > 0.001):
        beta = beta - (funct1(beta, data_array)/funct2(beta, data_array))
        print(beta, funct1(beta, data_array))

    return beta


data_array = list(range(1,11))
#data_array = [70.292, 10.107, 48.386, 20.480, 13.053, 25.292, 14.713, 39.166, 17.421, 13.905, 30.215, 17.137, 44.024, 10.552, 37.298, 16.314, 28.073, 39.019, 32.330, 36.547]
beta = beta_estimation(data_array)
print(beta)
sq_data_array = [i**2 for i in data_array]
print(sum(sq_data_array))
