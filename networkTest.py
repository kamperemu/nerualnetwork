from network import neuralNetwork



inputs = [[0,0],[0,1],[1,0],[1,1]]
outputs = [[0,0],[1,0],[1,0],[1,1]]

net = neuralNetwork(2,2,2,typeActivation="sigmoid")
net.train(inputs,outputs)
