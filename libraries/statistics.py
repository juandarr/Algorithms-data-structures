from math import factorial, sqrt

class Statistics:
    def __init__(self):
        pass

    @staticmethod
    def mean(ar, n):
        # Mean calculation
        mean = 0
        for i in ar:
            mean += i
        mean /= n
        return mean

    @staticmethod
    def median(ar, n):
        # Median calculation
        ar.sort()
        if n%2==0:
            median = (ar[int(n//2)-1]+ar[int(n//2)])/2
        else:
            median = ar[n//2][0]
        return median
    
    @staticmethod
    def modal(ar,n):
        value_frequency = {} 
        for i in ar:
            if i in value_frequency:
                value_frequency[i] += 1
            else:
                value_frequency[i] = 1

        # Modal calculation
        frequency_list = list(zip(value_frequency.keys(), value_frequency.values()))
        frequency_list.sort(key=lambda a:a[1], reverse=True)
        modal = frequency_list[0][0]
        frequency = frequency_list[0][1]
        for k in frequency_list[1:]:
            if k[1] == frequency:
                if k[0]< modal:
                    modal = k[0]
            else:
                break
        return modal

    @classmethod
    def std_dev(cls,ar, n):
        std_dev = 0
        for i in ar:
            std_dev += (i-cls.mean(ar,n))**2
        std_dev = sqrt(std_dev/n)
        return std_dev
    
    @classmethod
    def covariance(cls,x, y, n):
        x_mean = cls.mean(x,n)
        y_mean = cls.mean(y,n)
        cov = 0
        for i in range(n):
            cov += (x[i]-x_mean)*(y[i]-y_mean)
        cov /= n
        return cov
    
    @staticmethod
    def permutation(n,k):
        return factorial(n)/factorial(n-k)

    @staticmethod
    def combination(n,k):
        return factorial(n)/(factorial(n-k)*factorial(k))