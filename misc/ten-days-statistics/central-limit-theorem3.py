#!/bin/python3
import os
import math

def ndf(mean, std_dev, value):
    coef = -((value-mean)**2)/(2*std_dev**2)
    p = (1/(std_dev*math.sqrt(2*math.pi)))*math.e**(coef)
    return p

def ncdf(mean, std_dev, value):
    z = (value-mean)/(std_dev*math.sqrt(2))
    return 0.5*(1+math.erf(z))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mean = 500
    std_dev = 80/math.sqrt(100)

    A = (-1.96*std_dev+mean)
    B = (1.96*std_dev+mean)

    p = ncdf(mean, std_dev, B) - ncdf(mean, std_dev, A)

    fptr.write('{0:.2f}\n{1:.2f}'.format(A,B))

    fptr.close()