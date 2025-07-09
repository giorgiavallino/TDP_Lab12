import itertools
import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._countries = DAO.getAllNations()
        self._graph = nx.Graph()
        self._idMapRetailers = {}

    def buildGraph(self, stato, anno):
        self._graph.clear()
        retailers = DAO.getNodes(stato)
        self._createIdMapRetailers(retailers)
        self._graph.add_nodes_from(retailers)
        self.addEdges(anno)

    def _createIdMapRetailers(self, retailers):
        for retailer in retailers:
            self._idMapRetailers[retailer.Retailer_code] = retailer

    def addEdges(self, anno):
        for node_01, node_02 in itertools.combinations(self._graph.nodes, 2):
            arco = DAO.getEdge(anno, node_01, node_02)
            if arco is not None and arco[0] is not None and arco[1] is not None:
                self._graph.add_edge(self._idMapRetailers[arco[0]], self._idMapRetailers[arco[1]], weight=arco[2])

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()