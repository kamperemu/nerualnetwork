from layer import neuralLayer

class neuralNetwork:
    def __init__(self,*args,typeActivation):
        self.nl = []
        for i in range(len(args)-1):
            self.nl.append(neuralLayer(args[i],args[i+1],typeActivation))

net = neuralNetwork(4,5,6,typeActivation="sigmoid")