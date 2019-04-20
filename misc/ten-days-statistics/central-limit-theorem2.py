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

    mean = 2.4
    std_dev = 2.0/math.sqrt(100)

    value1 = 250/100
    p1 = ncdf(mean, std_dev, value1)

    fptr.write('{0:.4f}\n'.format(p1))

    fptr.close()