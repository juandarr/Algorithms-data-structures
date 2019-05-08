from math import cos,sin, pi
import numpy.linalg as algebra
import numpy as np

'''
Implementation of classes useful for Linear Algebra Study
'''
class Matrix:
    def __init__(self, mat):
        if type(mat)==type([]):
            if type(mat[0])==type([]):
                self.matrix = mat
            else:
                self.matrix = [[i] for i in mat]
        else:
            print('Input element must be a list or a list of lists.\n')


    def size(self):
        return [len(self.matrix), len(self.matrix[0])]

    def transpose(self):
        temp_matrix = [[] for i in range(len(self.matrix[0]))]
        for j in range(len(self.matrix[0])):
            for i in range(len(self.matrix)):
                temp_matrix[j].append(self.matrix[i][j])
        return Matrix(temp_matrix)

    def determinant(self):
        if (len(self.matrix)!=len(self.matrix[0])):
            print('Matrix is non-square.\n')
            return None
        if (len(self.matrix)==2 and len(self.matrix[0])==2):
            return (self.matrix[0][0]*self.matrix[1][1]-self.matrix[0][1]*self.matrix[1][0])
        elif (len(self.matrix)==3 and len(self.matrix[0])==3):
            a = self.matrix[1][1]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][1]
            b = - (self.matrix[1][0]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][0])
            c = self.matrix[1][0]*self.matrix[2][1] - self.matrix[1][1]*self.matrix[2][0]
            return (a*self.matrix[0][0] + b*self.matrix[0][1] + c*self.matrix[0][2])
        else:
            ar = np.array(self.matrix)
            determinant = algebra.det(ar)
            return determinant 

    def inverse(self):

        if (len(self.matrix)!=len(self.matrix[0])):
            print('Matrix is non-square.\n')
            return Matrix([[]])
        det = self.determinant()
        if (det==0):
            print('Matrix is non-singular/degenerate.\n')
            return Matrix([[]])
        
        if (len(self.matrix)==2 and len(self.matrix[0])==2):
            return (1/self.determinant())*Matrix([[self.matrix[1][1], -self.matrix[0][1]],[-self.matrix[1][0], self.matrix[0][0]]])
        elif (len(self.matrix)==3 and len(self.matrix[0])==3):
            a = self.matrix[1][1]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][1]
            b = - (self.matrix[1][0]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][0])
            c = self.matrix[1][0]*self.matrix[2][1] - self.matrix[1][1]*self.matrix[2][0]
            d = - (self.matrix[0][1]*self.matrix[2][2] - self.matrix[0][2]*self.matrix[2][1])
            e = self.matrix[0][0]*self.matrix[2][2] - self.matrix[0][2]*self.matrix[2][0]
            f = - (self.matrix[0][0]*self.matrix[2][1] - self.matrix[0][1]*self.matrix[2][0])
            g = self.matrix[0][1]*self.matrix[1][2] - self.matrix[0][2]*self.matrix[1][1]
            h = - (self.matrix[0][0]*self.matrix[1][2] - self.matrix[0][2]*self.matrix[1][0])
            i = self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
            return (1/self.determinant())*Matrix([[a,b,c],[d,e,f],[g,h,i]]).transpose()
        else:
            ar = np.array(self.matrix)
            ar_inv = algebra.inv(ar)
            return Matrix(ar_inv.tolist())

    
    def pw_prod(self, other):
        temp_matrix = [[] for i in range(len(self.matrix))]
        if len(other.matrix[0])==len(self.matrix[0]) and len(other.matrix)==len(self.matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    temp_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
            return Matrix(temp_matrix)
        else:
            print('Dimensions of matrices don\'t match: {0}x{1} and {2}x{3}'.format(len(self.matrix),len(self.matrix[0]),len(other.matrix),len(other.matrix[0])))

    def __add__(self, other):
        temp_matrix = [[] for i in range(len(self.matrix))]
        if len(other.matrix[0])==len(self.matrix[0]) and len(other.matrix)==len(self.matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    temp_matrix[i].append(self.matrix[i][j]*other.matrix[i][j])
            return Matrix(temp_matrix)
        else:
            print('Dimensions of matrices don\'t match: {0}x{1} and {2}x{3}'.format(len(self.matrix),len(self.matrix[0]),len(other.matrix),len(other.matrix[0])))
    
    def __sub__(self, other):
        temp_matrix = [[] for i in range(len(self.matrix))]
        if len(other.matrix[0])==len(self.matrix[0]) and len(other.matrix)==len(self.matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    temp_matrix[i].append(self.matrix[i][j] - other.matrix[i][j])
            return Matrix(temp_matrix)
        else:
            print('Dimensions of matrices don\'t match: {0}x{1} and {2}x{3}'.format(len(self.matrix),len(self.matrix[0]),len(other.matrix),len(other.matrix[0])))

    def __mul__(self,other):
        if type(other)!=type(Matrix([[]])):
            temp_matrix = [[] for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    temp_matrix[i].append(other*self.matrix[i][j]) 
            return Matrix(temp_matrix)
        else:
            if (len(self.matrix[0])==len(other.matrix)):
                temp_matrix = [[] for i in range(len(self.matrix))]
                for i in range(len(self.matrix)):
                    for j in range(len(other.matrix[0])):
                        value = 0
                        for k in range(len(self.matrix[0])):
                            value += self.matrix[i][k]*other.matrix[k][j]
                        temp_matrix[i].append(value) 
                return Matrix(temp_matrix)
            else:
                print('Number of columns of first matrix must be equal to the number of rows of the second matrix.\nInstead: {0}x{1} and {2}x{3}'.format(len(self.matrix),len(self.matrix[0]),len(other.matrix),len(other.matrix[0])))
    
    def __rmul__(self,other):
        if type(other)!=type(Matrix([[]])):
            temp_matrix = [[] for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    temp_matrix[i].append(other*self.matrix[i][j]) 
            return Matrix(temp_matrix)


    def __truediv__(self,other):
        temp_matrix = [[] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                temp_matrix[i].append(self.matrix[i][j]/other) 
        return Matrix(temp_matrix)

    def __neg__(self):
        temp_matrix = [[] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                temp_matrix[i].append(-self.matrix[i][j]) 
        return Matrix(temp_matrix)
    
    def __pos__(self):
        temp_matrix = [[] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                temp_matrix[i].append(+self.matrix[i][j]) 
        return Matrix(temp_matrix)
    
    def __repr__(self):
        s = ''
        for i in range(len(self.matrix)):
            s += '[ '
            for j in range(len(self.matrix[0])):
                if j < len(self.matrix[0])-1:
                    s += '{0:.2f}'.format(self.matrix[i][j]) + ' , ' 
                else:
                    s += '{0:.2f}'.format(self.matrix[i][j])
            if i < len(self.matrix)-1:
                s += ' ]\n'
            else: 
                s += ' ]'
        return s
    
    @classmethod
    def polarToVector(cls, mag : float, dir: float) -> 'Vector':
    	return cls([mag*cos((dir/180.0)*pi), mag*sin((dir/180.0)*pi)])

class Vector:
    def __init__(self, vec):
        self.array = vec

    def __add__(self, other):
        temp_array = []
        for i in range(len(self.array)):
            temp_array.append(self.array[i]+other.array[i])
        return Vector(temp_array)

    def __sub__(self, other):
        temp_array = []
        for i in range(len(self.array)):
            temp_array.append(self.array[i]-other.array[i])
        return Vector(temp_array)

    def __neg__(self):
        temp_array = []
        for i in range(len(self.array)):
            temp_array.append(-self.array[i])
        return Vector(temp_array)

    def __pos__(self):
        temp_array = []
        for i in range(len(self.array)):
            temp_array.append(+self.array[i])
        return Vector(temp_array)

    def __repr__(self):
        temp_string ='['
        for i in range(len(self.array)):
            if i < len(self.array)-1:
                temp_string += str(self.array[i]) + ' , '
            else:
                temp_string += str(self.array[i])
        temp_string += ']'
        return temp_string

    @classmethod
    def fromPar(cls, mag : float, dir: float) -> 'Vector':
    	return cls([mag*cos((dir/180.0)*pi), mag*sin((dir/180.0)*pi)])
