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
        
def rank(ar,n):
    zipped = zip(ar, [i for i in range(1,n+1)])
    ar_list = list(zipped)
    ar_list.sort(key= lambda a:a[0])
    rank = [0]*n
    for i in range(n):
        rank[ar_list[i][1]-1] = i+1
    return rank

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])


    x = list(map(float, input().rstrip().split()))
    y = list(map(float, input().rstrip().split()))

    x_rank = rank(x,n)
    y_rank = rank(y,n)
    
    x_std_dev = std_dev(x_rank,n)
    y_std_dev = std_dev(y_rank, n)
    cov = covariance(x_rank,y_rank,n)

    pearson_coefficient = cov/(x_std_dev*y_std_dev)

    fptr.write('{0:.3f}\n'.format(pearson_coefficient))

    fptr.close()
