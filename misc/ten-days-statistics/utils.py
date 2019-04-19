from math import *

class Collectables:
    def __init__(self):
        pass

    def perm(self,n,k):
        return factorial(n)/factorial(n-k)

    def comb(self, n,k):
        return self.perm(n,k)/factorial(k)

class Vector:
    def __init__(self, vec):
        self.x = vec[0]
        self.y = vec[1]
        
    def __add__(self, b):
        return Vector([self.x+b.x, self.y+b.y])

    def __sub__(self, b):
        return Vector([self.x-b.x, self.y-b.y])

    def __neg__(self):
        return Vector([-self.x, -self.y])

    def __pos__(self):
        return Vector([+self.x, +self.y])

    def __repr__(self):
        return '[{0} , {1}]'.format(self.x, self.y)

    @classmethod
    def fromPar(cls, mag : float, dir: float) -> 'Vector':
    	return cls([mag*cos((dir/180.0)*pi), mag*sin((dir/180.0)*pi)])
