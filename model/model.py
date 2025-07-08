import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._countries = DAO.getAllNations()
        self._graph = nx.Graph()

    def buildGraph(self, stato):
        self._graph.clear()
        stati = DAO.getNodes(stato)
        self._graph.add_nodes_from(stati)

    def getNumNodes(self):
        return self._graph.number_of_nodes()
