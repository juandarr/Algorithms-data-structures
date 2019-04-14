# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys

def sortSecond(arr):
    return arr[1]

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
    frequency_list.sort(key=sortSecond, reverse=True)
    modal = frequency_list[0][0]
    frequency = frequency_list[0][1]
    for k in frequency_list[1:]:
        if k[1] == frequency:
            if k[0]< modal:
                modal = k[0]
        else:
            break
    
    # Median calculation
    arr.sort()
    if n%2==0:
        median = (arr[int(n//2)-1]+arr[int(n//2)])/2
    else:
        median = arr[n//2][0]
    return mean, median, modal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])


    arr = list(map(int, input().rstrip().split()))
    mean, median, modal = statisticsValues(arr, n)

    fptr.write('{0:.1f}\n{1:.1f}\n{2}'.format(mean,median, modal))

    fptr.close()