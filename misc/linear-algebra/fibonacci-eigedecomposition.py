from math import sqrt
from utils import Matrix

def t(a,b,n):
    a11 = (2**(-n-1))*(a*(b**n)+b*((-a)**n))/sqrt(5)
    a12 = (2**(-n))*(b**n-((-a)**n))/sqrt(5)
    a21 = ((2**(-n-2))*a*b)*(b**n-((-a)**n))/sqrt(5)
    a22 = (2**(-n-1))*((b**(n+1))+((-a)**(n+1)))/sqrt(5)

    T = Matrix([[int(a11),int(a12)],[int(a21),int(a22)]])
    return T

if __name__ == '__main__':
    a = sqrt(5)-1
    b = sqrt(5)+1
    n = 1000
    for i in range(1,n+1):
        T = t(a,b,i)
        print('To the power of: {}'.format(i))
        print('{0}th element of the Fibonacci series: {1}'.format(i, T.matrix[0][0]))
        print(T)
