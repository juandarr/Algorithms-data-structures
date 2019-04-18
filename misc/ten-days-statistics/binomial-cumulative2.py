#!/bin/python3
import os
from math import factorial


# Complete the maximumToys function below.
def p_binomial(x, n, p):
   prob = ((factorial(n))/(factorial(x)*factorial(n-x)))*(p**x)*(1-p)**(n-x)
   return prob


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pn = input().split()

    p = float(pn[0])/100.0
    n = int(pn[1])
    print(p)
    print(n)
    cumulative1 = 0
    for i in range(0,3):
        cumulative1 += p_binomial(i,n,p)

    cumulative2 = 0
    for i in range(2,11):
        cumulative2 += p_binomial(i,n,p)

    fptr.write('{0:.3f}\n{1:.3f}'.format(cumulative1, cumulative2))

    fptr.close()


