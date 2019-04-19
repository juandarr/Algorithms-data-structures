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

    mean = 70
    std_dev = 10

    value2 = 60
    p3 = ncdf(mean, std_dev, value2)

    top = float('inf')

    p2 = ncdf(mean, std_dev, top) - p3

    value1 = 80

    p1 = ncdf(mean, std_dev, top) - ncdf(mean, std_dev, value1)

    fptr.write('{0:.2f}\n{1:.2f}\n{2:.2f}\n'.format(p1*100,p2*100,p3*100))

    fptr.close()