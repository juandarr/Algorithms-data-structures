#!/bin/python3
import os
import math



# Complete the maximumToys function below.
def poisson_distribution(lambda_val, k):
    p = (lambda_val**k)/((math.e**lambda_val*math.factorial(k)))
    return p


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lambda_val = 2.5
    k = 5
 
    p = poisson_distribution(lambda_val, k)


    fptr.write('{0:.3f}\n'.format(p))

    fptr.close()