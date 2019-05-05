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
        self.size = [input,output]
        self.hidden_size = []
        self.total_layers = 2
        self.init_weights()
        self.activations = []

    @staticmethod    
    def sigmoid(prod):
        for i in range(len(prod.matrix[0])):
            prod.matrix[0][i] = 1/(1+exp(-prod.matrix[0][i]))
        return prod

    '''
    Add hidden layer of dimension 'dimension'
    '''
    def add(self, dimension):
        self.hidden_size.append(dimension)
        self.total_layers += 1
        self.init_weights()

    def init_weights(self):
        self.theta = []
        layers_range = [self.size[0]]+ self.hidden_size + [self.size[-1]]
        for i in range(len(layers_range)-1):
            self.theta.append(Matrix([[random() for m in range(layers_range[i] + 1)] for n in range(layers_range[i+1])]))

    def getSize(self):
        return [self.size[0]]+ self.hidden_size + [self.size[-1]]

    '''
    Feed forward algorithm.
    Representation of data is one column (vector) per sample
    '''
    def feed_forward(self,x):
        output_data = Matrix(x).transpose()
        self.activations =[]
        for i in range(len(self.theta)):
            self.activations.append(output_data)
            input_data = Matrix(output_data.matrix.copy()).transpose()
            for j in range(len(input_data.matrix)):
                input_data.matrix[j] = [1] + input_data.matrix[j]
            output_data = self.sigmoid(self.theta[i] * input_data.transpose())
        self.activations.append(output_data)
        return output_data

    def back_propagation(self, x , y , lambda_r):
        Delta = [[[0 for i in range(len(self.theta[l].matrix[0]))] for j in range(len(self.theta[l].matrix))] for l in range(len(self.theta))]
        for m in range(len(x)):
            deltas = []
            self.feed_forward([x[m]])
            deltas.append((self.activations[-1]-Matrix([y[m]]))) 
            for l in range(len(self.theta)-1, 0, -1):
                deltas.insert(0,self.theta[l].transpose()*deltas[0])
            print(deltas)
        '''            
            for l in range(len(self.theta)):
                for j in range(len(self.theta[l].matrix)):
                    for i in range(len(self.theta[l].matrix[0])-1):
                        #self.activations[l].matrix[j][0]*deltas[l].matrix[i][0]
                        print('Activations: ',self.activations[l].matrix)
                        print('Deltas: ',deltas[l].matrix)
                        Delta[l][j][i] += (1)
        D = [[[0 for i in range(len(self.theta[l].matrix[0]))] for j in range(len(self.theta[l].matrix))] for l in range(len(self.theta))]
        for l in range(len(self.theta)):
            for j in range(len(self.theta[l].matrix)):
                for i in range(len(self.theta[l].matrix[0])):
                    if j==0:
                        D[l][j][i] = (1/len(x))*Delta[l][j][i]
                    else:
                        D[l][j][i] = (1/len(x))*Delta[l][j][i] +lambda_r * self.theta[l].matrix[j][i]
        '''
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
    #nn.theta[0].matrix[0] = [-15,10,10]
    x = [[0,0],[0,1],[1,0],[1,1]]
    y = [0,0,0,1]
    nn.add(5)
    print('Network size: {}'.format(nn.getSize()))
    print([(i[0],i[1]) for i in x])
    y_p = nn.feed_forward(x)
    print('Expected output: ', y)
    print('Predicted output: ',y_p)
    nn.back_propagation(x, y , 0.2)
    #for i in range(len(nn.activations)):
    #    print(i, nn.activations[i])
