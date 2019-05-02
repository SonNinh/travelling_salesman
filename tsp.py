import sys
import matplotlib.pyplot as plt
import numpy as np


class Node(object):
    def __init__(self, info):
        city_params = info.strip('\n').split(', ')
        self.city_name = city_params[0]
        self. coordinate = city_params[1:]


class Graph(object):
    def __init__(self, graph_dict=None):
        if not graph_dict:
            graph_dict = {}
        self._graph_dict = graph_dict

    def create_graph_dict(self, ls_of_cities):
        for city in ls_of_cities:
            city_params = city.strip('\n').split(', ')
            self._graph_dict[city_params[0]] = city_params[1:]


def main(ls_of_cities):
    my_map = Graph()
    my_map.create_graph_dict(ls_of_cities)
    # print(my_map._graph_dict)


if __name__ == "__main__":
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    print(x)

    plt.scatter(x, y)
    plt.show()
    with open(sys.argv[1]) as f:
        ls_of_cities = f.readlines()
        f.close()
        main(ls_of_cities)
