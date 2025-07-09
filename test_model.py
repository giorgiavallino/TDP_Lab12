from model.model import Model

myModel = Model()
myModel.buildGraph("Germany", 2016)
print(myModel.getNumNodes())
print(myModel.getNumEdges())
print(myModel.getEdgesAdjacent())
