import numpy as np

def compare_int(x, y):
    # TODO not implemented yet
    pass

def compare_lists(x, y):
    # TODO not implemented yet
    pass

def damereau_levenstein(x, y):
    d = np.zeros((len(x) + 1, len(y) + 1))

    d[:, 0] = np.arange(len(x) + 1)
    d[0, :] = np.arange(len(y) + 1)

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            sub_cost = int(x[i - 1] != y[j - 1])

            d[i, j] = min(
                    d[i - 1, j] + 1,
                    d[i, j - 1] + 1,
                    d[i - 1, j - 1] + sub_cost)

            if i > 1 and j > 1 and x[i - 1] == y[j - 2] and x[i - 2] == y[j - 1]:
                d[i, j] = min(
                        d[i, j],
                        d[i - 2, j - 2] + sub_cost)
    print(d)

    return d[len(x), len(y)]
