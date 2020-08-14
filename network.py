# imported neuralLayer so that we can use connection between layers in the network as objects instead of variables
from layer import neuralLayer

class neuralNetwork:

    # initialization of the network
    def __init__(self,*layerNoNeurons,typeActivation):
        # intialization of variables used
        self.layerNoNeurons = layerNoNeurons
        self.typeActivation = typeActivation
        # initialization of the connection of neural layers
        self.nl = []
        for i in range(len(layerNoNeurons)-1):
            self.nl.append(neuralLayer(layerNoNeurons[i],layerNoNeurons[i+1],self.typeActivation))

    # used for calculation of error in the backpropogation algorithm (NOTE: idk how the backprop algorithm works)
    def deriactivation(self, guess):
        if self.typeActivation == "sigmoid":
            guess = guess * (1 - guess)
        elif self.typeActivation == "ReLU":
            if guess > 0:
                guess = 1
            else:
                guess = 0
        return guess
        
    # calculates the values of output neurons by the feed forward algorithm
    def thinkOutput(self,inputs):   
        for i in range(len(self.nl)):
            # think function of nl calculates the values of next layer and then disposes of the previous layer values
            guess = []
            for j in range(len(inputs)):
                guess.append((self.nl[i].think(inputs[j])))
        return guess

    # calculates the values of all the hidden layer neurons (and output neurons) using the feed forward algorithm
    def thinkLayer(self,inputs):
        guess = []
        for i in range(len(self.nl)):
            # unlike thinkOutput it adds the previous layer values to the guess instead of disposing them
            guess.append([])
            for j in range(len(inputs)):
                guess[i].append((self.nl[i].think(inputs[j])))
        return guess
 
    # trains the neural network using backpropagation algorithm (NOTE: I should have really used numpy for the matrix maths)
    def train(self,inputs,targets):
        guess = self.thinkOutput(inputs)
        errors = []
        for i in range(len(targets)):
            errors.append([])
            for j in range(len(targets[i])):
                errors[i].append(targets[i][j]-guess[i][j])
        hiddenerrors = []
        
    


