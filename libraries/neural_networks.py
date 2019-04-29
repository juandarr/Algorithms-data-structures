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
        input_size = input
        output_size = output
        hidden_size = 0
        theta = Matrix([[random() for j in range(input_size)] for i in range(output_size)])

    @staticmethod    
    def sigmoid(x, theta):
        prod = theta*x
        for i in range(len(prod)):
            prod[i] = 1/(1+exp(-prod[i]))
        return prod

