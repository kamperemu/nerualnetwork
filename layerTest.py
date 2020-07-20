from layer import neuralLayer

inputs = [[0,0],[0,1],[1,0],[1,1]]
outputs = [[0,0],[1,0],[1,0],[1,1]]

layer = neuralLayer(2,2,"sigmoid")
layer.backProp(layer.think(inputs[0]))