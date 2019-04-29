from utils import Matrix
from random import random
from math import exp
'''
Neural network implementation using sigmoid as activation function.
Features:
    - Feed forward
    - Training with back propagation
'''

class NeuralNetworks:

    def __init__(self,input, output):
        self.input_size = input
        self.output_size = output
        self.hidden_size = 0
        self.theta = Matrix([[random() for j in range(self.input_size + 1)] for i in range(self.output_size)])

    @staticmethod    
    def sigmoid(prod):
        for i in range(len(prod.matrix[0])):
            prod.matrix[0][i] = 1/(1+exp(-prod.matrix[0][i]))
        return prod

    def feed_forward(self,x):
        for i in range(len(x)):
            x[i] = [1] + x[i]
        prod = self.sigmoid(self.theta * Matrix(x).transpose())
        return prod

    def back_propagation(self):
        pass

if __name__=='__main__':
    nn = NeuralNetworks(2,1)
    #print('\nNAND gate')
    #nn.theta.matrix[0] = [20,-15,-15]
    #print('\nNOR gate')
    #nn.theta.matrix[0] = [10,-15,-15]
    #print('\nOR gate')
    #nn.theta.matrix[0] = [-15,20,20]
    print('\nAND gate')
    y = [0,0,0,1]
    #nn.theta.matrix[0] = [-15,10,10]
    x = [[0,0],[1,0],[0,1],[1,1]]
    print([(i[0],i[1]) for i in x])
    y = nn.feed_forward(x)
    print(y)
