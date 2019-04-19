from math import cos,sin, pi

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


    def getsize(self):
        return [len(self.matrix), len(self.matrix[0])]

    def __add__(self, other):
        temp_matrix = [[] for i in range(len(self.matrix))]
        if len(other.matrix[0])==len(self.matrix[0]) and len(other.matrix)==len(self.matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    temp_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
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
        if (len(self.matrix[0])==len(other.matrix)):
            temp_matrix = [[] for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    value = 0
                    for k in range(len(self.matrix[0])):
                        value += self.matrix[i][k]*other.matrix[k][j]
                    temp_matrix[i].append(value) 
            return Matrix(temp_matrix)

    def __rmul__(self,other):
        if type(other)!=type([]):
            temp_matrix = [[] for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    temp_matrix[i].append(other*self.matrix[i][j]) 
            return Matrix(temp_matrix)
        else:
            if (len(self.matrix)==len(other.matrix[0])):
                temp_matrix = [[] for i in range(len(other.matrix))]
                for i in range(len(other.matrix)):
                    for j in range(len(self.matrix[0])):
                        value = 0
                        for k in range(len(other.matrix[0])):
                            value += other.matrix[i][k]*self.matrix[k][j]
                        temp_matrix[i].append(value) 
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
