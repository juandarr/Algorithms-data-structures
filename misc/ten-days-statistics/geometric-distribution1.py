#!/bin/python3
import os



# Complete the maximumToys function below.
def p_geometric(n, p):
   prob = (p)*((1-p)**(n-1))
   return prob


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')


    p = 1.0/3.0
    n = 5
    prob = p_geometric(n,p)


    fptr.write('{0:.3f}\n'.format(prob))

    fptr.close()