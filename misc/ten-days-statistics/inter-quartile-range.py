#!/bin/python3
import os

def sortFirst(a):
    return a[0]

def calculateQuartile(arr,n):
    if n%2==0:
        q = (arr[n//2-1]+arr[n//2])/2
    else:
        q = arr[n//2]
    return q

# Complete the maximumToys function below.
def interQuartileRange(arr, freq):
    zipped = zip(arr,freq)
    z_list = list(zipped)
    z_list.sort(key = sortFirst)
    a = []
    for c in z_list:
        for i in range(c[1]):
            a.append(c[0])
    n =len(a)
    shift = 0
    if n%2!=0:
        # If array length is odd we need to ignore the value in the middle
        # So, move starting index one element to the right
        shift = 1
    q1 = calculateQuartile(a[0:n//2-1], n//2)
    q3 = calculateQuartile(a[n//2+shift:], n//2)
    return (q3-q1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    arr = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    inter_range = interQuartileRange(arr, freq)

    fptr.write('{0:.1f}\n'.format(inter_range))

    fptr.close()