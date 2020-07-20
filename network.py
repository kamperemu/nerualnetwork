from layer import neuralLayer

class neuralNetwork:
    def __init__(self,*layerNoNeurons,typeActivation):
        self.layerNoNeurons = layerNoNeurons
        self.typeActivation = typeActivation
        self.nl = []
        for i in range(len(layerNoNeurons)-1):
            self.nl.append(neuralLayer(layerNoNeurons[i],layerNoNeurons[i+1],self.typeActivation))

    
        
    def thinkOutput(self,inputs):
        for i in range(len(self.nl)):
            guess = []
            for j in range(len(inputs)):
                guess.append((self.nl[i].think(inputs[j])))
        return guess

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
        guess = self.thinkOutput(inputs)
        print(guess)
        for i in layer:
            print(i)
        


