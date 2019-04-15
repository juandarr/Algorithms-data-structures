#!/bin/python3
import os


def calculateQuartile(arr,n):
    if n%2==0:
        q = (arr[n//2-1]+arr[n//2])/2
    else:
        q = arr[n//2]
    return q

# Complete the maximumToys function below.
def quartiles(arr, n):
    arr.sort()
    q2 = calculateQuartile(arr,n)
    shift = 0
    if n%2!=0:
        shift = 1
    q1 = calculateQuartile(arr[0:n//2-1], n//2)
    q3 = calculateQuartile(arr[n//2+shift:], n//2)
    return q1, q2, q3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    arr = list(map(int, input().rstrip().split()))
    q1, q2, q3 = quartiles(arr, n)

    fptr.write('{0:.0f}\n{1:.0f}\n{2:.0f}'.format(q1,q2,q3))

    fptr.close()
