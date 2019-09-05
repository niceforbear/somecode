"""
Author: ykliu
Date: 2019/9/6 00:58
"""

from numpy import *


def to_int(to_int_array):
    """
    Because some data is string type when it's loaded from files. Sometimes we require to transform data to int type.

    :param to_int_array: array
    :return: array
    """
    to_int_array = mat(to_int_array)
    m, n = shape(to_int_array)
    new_array = zeros((m, n))
    for i in range(m):
        for j in range(n):
            new_array[i, j] = int(to_int_array[i, j])

    return new_array


if __name__ == "__main__":
    arr = [[1.1, 2.2], [2.333, 0.3]]
    trans_arr = array(arr)
    res = to_int(trans_arr)
    print(res)
