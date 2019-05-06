from math import sqrt
import sys
from time import time
from matplotlib import pyplot
# from mpl_toolkits.mplot3d import Axes3D


def get_distance(node_a, node_b):
    return sqrt((node_a[0]-node_b[0])**2 + (node_a[1]-node_b[1])**2)


class Graph():

    def __init__(self, vertices, ls_of_nodes):
        self.v = vertices
        self.graph = []
        self._create_graph(ls_of_nodes[:vertices])
        a = 1

    def _create_graph(self, ls_of_nodes):
        for indx_a, node_a in enumerate(ls_of_nodes):
            temp = []
            for node_b in ls_of_nodes[:indx_a]:
                # print(node_a)
                temp.append(get_distance(node_a, node_b))
            self.graph.append(temp)
            # print(self.graph)

    def _update_min(self, node_idx, nearest_to_each_node, ls_of_included):
        min = sys.maxsize
        for idx, d in enumerate(self.graph[node_idx]):
            if ls_of_included[idx] is False and min > d:
                min = d
                min_idx = idx
        for row in range(node_idx+1, self.v):
            # print("row:", row)
            # print("node_idx:", node_idx)
            if ls_of_included[row] is False and min > self.graph[row][node_idx]:
                min = self.graph[row][node_idx]
                min_idx = row
        nearest_to_each_node[node_idx] = [min_idx, min]

    def Prim_mst(self):
        # self.graph = [[],
        #               [2],
        #               [0, 3],
        #               [6, 8, 0],
        #               [0, 5, 7, 9]]
        mst = [0]
        ls_of_included = [False] * self.v
        ls_of_included[0] = True
        nearest_to_each_node = [[i, sys.maxsize] for i in range(self.v)]
        count = 0
        while count < self.v-1:
            count += 1
            for i, each in enumerate(ls_of_included):
                if each and nearest_to_each_node[i][0] == i:
                    self._update_min(i, nearest_to_each_node, ls_of_included)
                # else:
                #     print("asd")
            nearest_node = ls_of_included.index(True)
            for i, each in enumerate(ls_of_included):
                if nearest_to_each_node[i][1] < nearest_to_each_node[nearest_node][1] and each:
                    nearest_node = i

            first = mst.index(nearest_node)
            # if first != len(mst)-1:
            #     mst.insert(first+1, nearest_node)
            mst.insert(first+1, nearest_to_each_node[nearest_node][0])

            # print("at:", nearest_to_ each_node[nearest_node][0])
            # print(mst)
            ls_of_included[nearest_to_each_node[nearest_node][0]] = True
            for idx, each in enumerate(ls_of_included):
                if each is True:
                    nearest_to_each_node[idx] = [idx, sys.maxsize]
            # print(ls_of_included)
            # print(nearest_to_each_node)
        res = 0
        for i in range(len(mst)-1):
            if mst[i] > mst[i+1]:
                res += self.graph[mst[i]][mst[i+1]]
            else:
                res += self.graph[mst[i+1]][mst[i]]
        print("cost:", res)

        print(mst)
        print(len(mst))
        return mst


def main(ls_of_cities):
    # fig = pyplot.figure()
    # ax = Axes3D(fig)

    start = time()
    ls_of_nodes = []
    for city in ls_of_cities:
        ls_of_nodes.append(list(map(float, city[:-1].split(', ')[1:])))
    
    # for node in ls_of_nodes:
    #     pyplot.scatter(node[1], node[0], c='red')

    # pyplot.show()
    g = Graph(len(ls_of_nodes), ls_of_nodes)
    # print("graph time:", time()-start)
    # print(ls_of_nodes)
    # g = Graph(10, ls_of_nodes)
    # start = time()
    # print("prim time:", time()-start)
    # return g.Prim_mst(), g

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        ls_of_cities = f.readlines()
        result, g = main(ls_of_cities)
        for city in result:
            print(ls_of_cities[city][:-1])
