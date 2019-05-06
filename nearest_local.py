import sys
from time import time
import matplotlib.pyplot as plt
from math import sqrt
from sys import maxsize
from plot import plot


def get_dist(pa, pb):
    return sqrt((pa[0]-pb[0])**2 + (pa[1]-pb[1])**2)


def find_start_node(start_node, sorted_x):
    for i, c in enumerate(sorted_x):
        if start_node == c[2]:
            return i
        

def main(ls_of_cities):
    # fig = pyplot.figure()
    # ax = Axes3D(fig)
    vetex = len(ls_of_cities)
    cost = 0
    start = time()
    path = []
    ls_of_nodes = []
    points = []

    for idx, city in enumerate(ls_of_cities):
        each = list(map(float, city[:-1].split(', ')[1:]))
        points.append(each[::-1])
        each.append(idx)
        ls_of_nodes.append(each)
        
        # ls_of_nodes[-1].append(idx)
    
    # for node in ls_of_nodes:
    #     pyplot.scatter(node[1], node[0], c='red')
    # pyplot.show()
    # print(ls_of_nodes[:10])
    sorted_x = sorted(ls_of_nodes,key=lambda l:l[0])
    # sorted_y = sorted(ls_of_nodes,key=lambda l:l[1])
    # print(sorted_x[:100])
    # print(sorted_y[:100])
    print('data-prepared time:', time()-start)
    start = time()
    cur_city = 0
    x_id = find_start_node(cur_city, sorted_x)
    while True:
        # print(x_id, y_id)
        delta = 8.0
        ls_of_common = set()

        x_ref = sorted_x[x_id][0]
        # y_ref = sorted_y[y_id][1]
        y_ref = sorted_x[x_id][1]
        # print('x,y:', x_ref,y_ref)
        while not ls_of_common:
            delta += 0.1
            ls_x = []
            # ls_y = []
            buffer_x = []
            # buffer_y = []


            for i in range(x_id+1, len(sorted_x)):
                if sorted_x[i][0] <= x_ref + delta:
                    if sorted_x[i][1] <= y_ref + delta and sorted_x[i][1] >= y_ref - delta:
                        ls_x.append(sorted_x[i][2])
                        buffer_x.append(i)
                else:
                    break

            for i in range(x_id-1, -1, -1):
                if sorted_x[i][0] >= x_ref - delta:
                    if sorted_x[i][1] <= y_ref + delta and sorted_x[i][1] >= y_ref - delta:
                        ls_x.append(sorted_x[i][2])
                        buffer_x.append(i)
                else:
                    break
            
            # for i in range(y_id+1, len(sorted_y)):
            #     if sorted_y[i][1] <= y_ref + delta:
            #         ls_y.append(sorted_y[i][2])
            #         buffer_y.append(i)
            #     else:
            #         break

            # for i in range(y_id-1, -1, -1):
            #     if sorted_y[i][1] >= y_ref - delta:
            #         ls_y.append(sorted_y[i][2])
            #         buffer_y.append(i)
            #     else:
            #         break

            # ls_of_common = find_common(ls_x, ls_y)
            ls_of_common = ls_x
        # print(ls_of_common)
        min_dist = maxsize
        min_id = None
        
        for city_id in ls_of_common:
            dist = get_dist(ls_of_nodes[city_id], ls_of_nodes[cur_city])
            if dist < min_dist:
                min_dist = dist
                min_id = city_id
        if min_id:
            cost += min_dist
            # print("min", min_dist)
            path.append(min_id)
            # print(ls_of_cities[min_id])
            # print(delta)
            sorted_x.pop(x_id)
            # sorted_y.pop(y_id)
            cur_city = min_id

            new_x_id = buffer_x[ls_x.index(min_id)]
            # new_y_id = buffer_y[ls_y.index(min_id)]

            if new_x_id > x_id:
                new_x_id -= 1
                # print("a")
            # if new_y_id > y_id:
            #     new_y_id -= 1
                # print("b")

            # x_id, y_id = new_x_id, new_y_id
            x_id = new_x_id
            # print("xy_id:", x_id, y_id)
            # print(len(path))
            if len(path) == vetex-1:
                print("cost:", cost)
                break
        else:
            break
    
    print('time:', time()-start)
    plot(points, path)
    


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        ls_of_cities = f.readlines()
        main(ls_of_cities)
        # for city in result:
        #     print(ls_of_cities[city][:-1])