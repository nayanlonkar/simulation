#program to generate a random variate generation for exponential distribution
import random
import math

#this function will lamda(i.e 1/mean) and return a random variate
def random_exponetial(lamda):
    rand_number = (-1/lamda) * math.log(1 - random.random())
    return rand_number

print(random_exponetial(1))


