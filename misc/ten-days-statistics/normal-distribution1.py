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

    mean = 20
    std_dev = 2

    value1 = 19.5
    p1 = ncdf(mean, std_dev, value1)

    value2 = 20
    value3 = 22

    p2 = ncdf(mean, std_dev, value3) - ncdf(mean, std_dev, value2)

    fptr.write('{0:.3f}\n{1:.3f}\n'.format(p1,p2))

    fptr.close()