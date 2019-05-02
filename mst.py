import sys
from math import sqrt


#Class to represent a graph 
class Graph: 

    def __init__(self,vertices): 
        self.V= vertices
        self.graph = []

    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, x, y): 
        if x < y: 
            parent[x] = y
        else: 
            parent[y] = x 

    def KruskalMST(self): 

        result =[] #This will store the resultant MST 

        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 

        self.graph = sorted(self.graph,key=lambda item: item[2]) 

        parent = []

        # Create V subsets with single elements 
        for node in range(self.V):
            parent.append(node)

        # Number of edges to be taken is equal to V-1
        while e < self.V -1 :
            # print(i)
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w]) 
                print ("%d -- %d == %f" %(u,v,w))
                self.union(parent, x, y) 
        
        

def get_distance(node_a, node_b):
	return sqrt((node_a[0]-node_b[0])**2 + (node_a[1]-node_b[1])**2)


def main(ls_of_cities):
    ls_of_nodes = []
    for city in ls_of_cities:
        ls_of_nodes.append(list(map(float, city[:-1].split(', ')[1:])))
    g = Graph(len(ls_of_nodes))
    # g = Graph(4)
    # print(ls_of_nodes)
    for indx_a, node_a in enumerate(ls_of_nodes):
        for indx_b, node_b in enumerate(ls_of_nodes[indx_a+1:]):
            g.addEdge(indx_a, indx_b+indx_a+1, get_distance(node_a, node_b))
            # get_distance(node_a, node_b)
    g.KruskalMST()


if __name__ == "__main__":
    # N = 50
    # x = np.random.rand(N)
    # y = np.random.rand(N)
    # print(x)

    # plt.scatter(x, y)
    # plt.show()
    with open(sys.argv[1]) as f:
        ls_of_cities = f.readlines()
        f.close()
        main(ls_of_cities)