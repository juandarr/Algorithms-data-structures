#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # Brute force - Doesn't work for big data, time complexity O(N^2)
    '''
    z = [0]*n
    max_val = 0

    for q in queries:
        for i in range(q[0]-1, q[1]):
            z[i] += q[2]
            if z[i] > max_val:
                max_val = z[i]

    return max_val
    '''
    # More efficient version. Time complexity O(N+M)
    z = [0]*n
    max_val = 0

    for q in queries:
        z[q[0]-1] = z[q[0]-1]+ q[2]
        if (q[1]<n):
            z[q[1]] = z[q[1]]-q[2]

    accumulator = 0
    for i in z:
        accumulator += i
        if accumulator > max_val:
            max_val = accumulator
    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()