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
        self.theta = Matrix([[random() for j in range(self.input_size)] for i in range(self.output_size)])

    @staticmethod    
    def sigmoid(x, theta):
        prod = theta*x
        for i in range(len(prod)):
            prod[i] = 1/(1+exp(-prod[i]))
        return prod

