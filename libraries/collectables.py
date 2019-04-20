from math import factorial

class Collectables:
    def __init__(self):
        pass

    @staticmethod
    def perm(n,k):
        return factorial(n)/factorial(n-k)

    @staticmethod
    def comb(n,k):
        return factorial(n)/(factorial(n-k)*factorial(k))