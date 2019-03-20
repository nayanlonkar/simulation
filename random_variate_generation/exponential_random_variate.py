#program to generate a random variate for exponential distribution
#inverse transformation technique is used here
import random
import math

#this function will lamda(i.e 1/mean) and return a random variate
#random.random() returns the random number between 0 and 1
def random_exponetial(lamda):
    rand_variate = (-1/lamda) * math.log(1 - random.random())
    return rand_variate

data_array = [random_exponetial(1) for _ in range(100)]
print(data_array)

