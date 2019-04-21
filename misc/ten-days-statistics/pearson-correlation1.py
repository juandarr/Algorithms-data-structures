import os
from math import sqrt

def mean(ar, n):
        # Mean calculation
        mean = 0
        for i in ar:
            mean += i
        mean /= n
        return mean

def std_dev(ar, n):
        std_dev = 0
        for i in ar:
            std_dev += (i-mean(ar,n))**2
        std_dev = sqrt(std_dev/n)
        return std_dev

def covariance(x, y, n):
        x_mean = mean(x,n)
        y_mean = mean(y,n)
        cov = 0
        for i in range(n):
            cov += (x[i]-x_mean)*(y[i]-y_mean)
        cov /= n
        return cov

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])


    x = list(map(float, input().rstrip().split()))
    y = list(map(float, input().rstrip().split()))

    x_std_dev = std_dev(x,n)
    y_std_dev = std_dev(y, n)
    cov = covariance(x,y,n)

    pearson_coefficient = cov/(x_std_dev*y_std_dev)

    fptr.write('{0:.3f}\n'.format(pearson_coefficient))
    
    fptr.close()