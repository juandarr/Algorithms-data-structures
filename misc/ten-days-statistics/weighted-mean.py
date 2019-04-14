#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def weightedMean(ar, w):
    num = 0
    den = 0
    for i in zip(ar,w):
        num += i[0]*i[1]
        den += i[1]
    return num/den


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nw = input().split()

    n = int(nw[0])

    tmp = []
    for _ in range(2):
        tmp.append(list(map(int, input().rstrip().split())))
    
    arr = tmp[0]
    weights = tmp[1]

    weighted_mean = weightedMean(arr, weights)

    fptr.write('{0:.1f}\n'.format(weighted_mean))

    fptr.close()
