#!/bin/python3
import os
from math import factorial


# Complete the maximumToys function below.
def p_binomial(x, n, p):
   prob = ((factorial(n))/(factorial(x)*factorial(n-x)))*(p**x)*(1-p)**(n-x)
   return prob


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bg = input().split()

    b = float(bg[0])
    g = float(bg[1])

    p = b/(b+g)
    cumulative = 0
    for i in range(3,7):
        cumulative += p_binomial(i,6,p)

    fptr.write('{0:.3f}\n'.format(cumulative))

    fptr.close()