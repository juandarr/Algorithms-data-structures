#!/bin/python3
import os

from math import sqrt

# Calculates the standard deviation
def standardDeviation(arr, n):
    mean = 0
    for i in arr:
        mean += i
    mean /= n
    std_dev = 0
    for i in arr:
        std_dev += (i-mean)**2
    std_dev = sqrt(std_dev/n)


    return std_dev

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])


    arr = list(map(int, input().rstrip().split()))
    std_dev= standardDeviation(arr, n)

    fptr.write('{0:.1f}\n'.format(std_dev))

    fptr.close()
