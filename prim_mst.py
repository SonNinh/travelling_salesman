from math import sqrt
import sys
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


def get_distance(node_a, node_b):
	return sqrt((node_a[0]-node_b[0])**2 + (node_a[1]-node_b[1])**2)


class Graph():

    def __init__(self,vertices, ls_of_nodes): 
        self.V= vertices
        self.graph = []
        self._create_graph(ls_of_nodes[:vertices])

    def _create_graph(self, ls_of_nodes):
        for indx_a, node_a in enumerate(ls_of_nodes):
            temp = []
            for node_b in ls_of_nodes[:indx_a]:
                # print(node_a)
                temp.append(get_distance(node_a, node_b))
            self.graph.append(temp)
        # print(self.graph)
    
    def Prim_mst(self):
        mst = []
        ls_of_included = [0]
        min
        for node_idx in ls_of_included:
            self.graph[node_idx]


def main(ls_of_cities):
    ls_of_nodes = []
    for city in ls_of_cities:
        ls_of_nodes.append(list(map(float, city[:-1].split(', ')[1:])))
    
    # g = Graph(len(ls_of_nodes), ls_of_nodes)
    # print(ls_of_nodes)
    g = Graph(4, ls_of_nodes)
    


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        ls_of_cities = f.readlines()
        f.close()
        main(ls_of_cities)