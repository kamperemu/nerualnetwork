import numpy as np
import random, os


# class for the main neural network which is Perceptron
class neuralLayer:

    # intializaition of the variables
    def __init__(self,noInputNeurons,noOutputNeurons,typeActivation):

        # bias will later be randomized with the last weight
        self.bias = 1
        self.typeActivation = typeActivation
        self.noInputNeurons = noInputNeurons
        self.noOutputNeurons = noOutputNeurons
        # weights are randomized
        self.weights = []
        for j in range(noOutputNeurons):
            self.weights.append([])
            for i in range(noInputNeurons+1):
                self.weights[j].append(random.random())
    
    # calculate the next layer (NOTE: I know its a bad explanation of what the function does)
    def activation(self,guess):
        if self.typeActivation == "sigmoid":
            guess = 1/(1+np.exp(-guess))
        elif self.typeActivation == "ReLU":
            guess = np.maximum(0,guess)
        return guess

    

    # the calculations that need to be done for finding the value of the next layer
    def think(self,inputs):

        # summation of the product of weights and input neurons (NOTE: I could have done it with dot method in numpy)
        summation = []
        for i in range(self.noOutputNeurons):
            summation.append(0)
            for j in range(self.noInputNeurons+1):
                # first we add the inputs with the product of weights and the input and the final one is the product of weight and bias
                try:
                    summation[i] += inputs[j] * self.weights[i][j]
                except IndexError:
                    summation[i] += self.bias * self.weights[i][j]


            # we find the activation of the required summation
            summation[i] = self.activation(summation[i])
        return summation
