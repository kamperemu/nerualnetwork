from layer import neuralLayer

class neuralNetwork:
    def __init__(self,*args):
        self.nl = []
        for i in range(1,len(args)-1):
            self.nl[i] = neuralLayer(args[i-1],args[i],"step")

net = neuralNetwork(4,5,6)