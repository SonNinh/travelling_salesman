import operator
import matplotlib.pyplot as plt


def plot(points, path: list):
    x = []
    y = []
    for point in points:
        y.append(point.x)
        x.append(point.y)
    # y = list(map(operator.sub, [max(y) for i in range(len(points))], y))
    plt.plot(x[0], y[0], 'bo')
    plt.plot(x[1:], y[1:], 'co')
    plt.plot(x[path[-1]], y[path[-1]], 'bo')

    for _ in range(1, len(path)):
        i = path[_ - 1]
        j = path[_]
        plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], color='r', length_includes_head=True)

    # plt.xlim(0, max(x) * 1.1)
    # # noinspection PyTypeChecker
    # plt.gca().invert_yaxis()
    plt.show()
