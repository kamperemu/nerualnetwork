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
            inputs = self.nl[i].think(inputs)
        return inputs

    def thinkLayer(self,inputs):
        layer = []
        layer.append(inputs)
        for i in range(len(self.nl)):
            layer.append(self.nl[i].think(inputs))
        return layer


    def train(self,inputs,outputs):
        layerTEMP = []
        for i in inputs:
            layerTEMP.append(self.thinkLayer(i))
        layer = []
        for i in range(len(self.layerNoNeurons)):
            layer.append([])
            for j in range(len(inputs)):
                layer[i].append(layerTEMP[j][i])
        
        

            
                


net = neuralNetwork(2,2,2,2,typeActivation="sigmoid")

inputs = [[0,0],[0,1],[1,0],[1,1]]
outputs = [[0,0],[1,0],[1,0],[1,1]]


net.train(inputs,outputs)