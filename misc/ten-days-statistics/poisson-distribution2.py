#!/bin/python3
import os
import math

def expected_x2(lambda_val):
    return lambda_val+lambda_val**2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lambda_val_a = 0.88
    lambda_val_b = 1.55

    c_a = 160 + 40*expected_x2(lambda_val_a)
    c_b = 128 + 40*expected_x2(lambda_val_b)


    fptr.write('{0:.3f}\n{1:.3f}\n'.format(c_a, c_b))

    fptr.close()
