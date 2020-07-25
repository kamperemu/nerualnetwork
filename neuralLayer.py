import numpy as np
import random, os


# class for the main neural network which is Perceptron
class neuralLayer:

    # intializaition of the variables
    def __init__(self, noInputNeurons, noOutputNeurons,typeActivation):

        # bias will later be randomized with the last weight
        self.bias = 1
        self.typeActivation = typeActivation

        # weights are randomized
        self.weights = []
        for j in range(noOutputNeurons):
            weightNeuron = []
            for i in range(noInputNeurons+1):
                weightNeuron.append(random.random())
            self.weights.append(weightNeuron)
            

    # this is the function being used for the data so that we can fit the neural network
    def activation(self,guess):
        if self.typeActivation == "sigmoid":
            guess = 1/(1+np.exp(-guess))
        elif self.typeActivation == "ReLU":
            guess = np.maximum(0,guess)
        return guess
            
    def deriactivation(self, guess):
        if self.typeActivation == "sigmoid":
            guess = guess * (1 - guess)
        elif self.typeActivation == "ReLU":
            if guess > 0:
                guess = 1
            else:
                guess = 0
        return guess

    def train(self, inputs, outputs,noOutputNeurons):

        # goes through all the inputs and outputs
        for i in range(len(outputs)):

            # we find the error in the neural network
            guess = self.think(inputs[i],noOutputNeurons)
            for j in range(noOutputNeurons):

                error = outputs[i][j] - guess[j]



                # weights are adjusted according to the error in the neural network
                for k in range(len(self.weights)):
                    # first we change the errors of the weights of inputs and then for the bias
                    try:
                        self.weights[j][k] += error * inputs[i][j] 
                    except IndexError:
                        self.weights[j][k] += error * self.bias 


    # the calculations that need to be done for finding the value of the next neuron
    def think(self,inputs,noOutputNeurons):

        # summation of the product of weights and input neurons (NOTE: I could have done it with dot method in numpy)
        sum = []
        for j in range(noOutputNeurons):
            sum.append(0)
    
            for i in range(len(self.weights)):
                # first we add the inputs with the products and the final one is the product of weight and bias
                try:
                    sum[j] += inputs[i] * self.weights[j][i]
                except IndexError:
                    sum[j] += self.bias * self.weights[j][i]
            
            self.activation(sum[j])


        # we find the activation of the required summation
        return sum
        

