from layer import neuralLayer

class neuralNetwork:
    def __init__(self,*layerNoNeurons,typeActivation):
        self.layerNoNeurons = layerNoNeurons
        self.typeActivation = typeActivation
        self.nl = []
        for i in range(len(layerNoNeurons)-1):
            self.nl.append(neuralLayer(layerNoNeurons[i],layerNoNeurons[i+1],self.typeActivation))

    def deriactivation(self, guess):
        if self.typeActivation == "sigmoid":
            guess = guess * (1 - guess)
        elif self.typeActivation == "ReLU":
            if guess > 0:
                guess = 1
            else:
                guess = 0
        return guess
        
    def thinkOutput(self,inputs):   
        for i in range(len(self.nl)):
            guess = []
            for j in range(len(inputs)):
                guess.append((self.nl[i].think(inputs[j])))
        return guess

    def thinkLayer(self,inputs):
        guess = []
        for i in range(len(self.nl)):
            guess.append([])
            for j in range(len(inputs)):
                guess[i].append((self.nl[i].think(inputs[j])))
        return guess
 

    def backprop_error(self,inputs,outputs):
        network = ['output':self.thinkLayer(inputs),'weights':self.nl[i].weights for i in range(len(self.nl))]
        print(network)
        for i in reversed(range(len(network)):
            layer = network[i]
            errors = []
            if i != len(network)-1:
                for j in range(len(layer)):
                    error = 0

    
    def train(self,inputs,outputs):
        self.backprop_error(outputs)


