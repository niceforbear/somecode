"""
Author: ykliu
Date: 2019/9/6 00:59
"""
from numpy import shape, array as np_array


def normalizing(array):
    m, n = shape(array)
    for i in range(m):
        for j in range(n):
            if array[i, j] != 0:
                array[i, j] = 1

    return array


if __name__ == "__main__":
    test_data = [[1, 2], [2, 0]]
    test_arr = np_array(test_data)
    res = normalizing(test_arr)
    print(res)
