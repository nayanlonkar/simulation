#program to generate a random variate for weibull distribution
#inverse transformation technique is used here.
import random
import math

#this function accepts alpha and beta and
#returns a random variate

def random_weibull(alpha, beta):
    rand_variate = -1 * (math.log( 1 - random.random()))
    rand_variate = rand_variate ** (1/beta)
    rand_variate = rand_variate * alpha
    return rand_variate

data_array = [random_weibull(0.5,2) for _ in range(100)]
print(data_array)

