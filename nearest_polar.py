import sys
from math import sqrt, atan2
import matplotlib.pyplot as plt


def main(ls_of_cities):
    ls_of_nodes = []
    start_node = list(map(float, ls_of_cities[0][:-1].split(', ')[1:]))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')

    for city in ls_of_cities:
        cartesian = list(map(float, city[:-1].split(', ')[1:]))
        r = sqrt((cartesian[0]-start_node[0])**2 + (cartesian[1]-start_node[1])**2)
        alpha = atan2(cartesian[0]-start_node[0], cartesian[1]-start_node[1])
        ls_of_nodes.append([r, alpha])

        c = ax.scatter(alpha, r, c='red', alpha=1)
    
    plt.show()

    
if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        ls_of_cities = f.readlines()
        result, g = main(ls_of_cities)
        for city in result:
            print(ls_of_cities[city][:-1])