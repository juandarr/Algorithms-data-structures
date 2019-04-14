#!/bin/python3

import math
import os
import random
import re
import sys

def sortFirst(arr):
    return arr[0]

# Complete the maximumToys function below.
def statisticsValues(arr, n):

    # Mean calculation
    mean = 0
    value_frequency = {} 
    for i in arr:
        if i in value_frequency:
            value_frequency[i] += 1
        else:
            value_frequency[i] = 1
        mean += i
    mean /= n

    # Modal calculation
    frequency_list = list(zip(value_frequency.keys(), value_frequency.values()))
    frequency_list.sort(key=sortFirst)
    frequency = 0
    for k in frequency_list:
        if k[1] > frequency:
            modal = k[0]
            frequency = k[1]
    
    # Median calculation
    if n%2==0:
        median = (frequency_list[int(n//2-1)][0]+frequency_list[int(n//2)][0])/2
    else:
        median = frequency_list[n//2][0]
    return mean, median, modal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])


    arr = list(map(int, input().rstrip().split()))
    mean, median, modal = statisticsValues(arr, n)

    fptr.write('{0:.1f}\n{1:.1f}\n{2}\n'.format(mean,median, modal))

    fptr.close()