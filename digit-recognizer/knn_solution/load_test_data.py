"""
Author: ykliu
Date: 2019/9/6 01:07
"""
import csv
from numpy import array
from normalizing import normalizing
from utils import to_int
from logger import log


def load_test_data(test_file):
    load_list = []
    log("Start load test data")
    with open(test_file, "r") as f:
        lines = csv.reader(f)
        for line in lines:
            load_list.append(line)

    load_list.remove(load_list[0])
    data = array(load_list)

    return normalizing(to_int(data))


def load_test_result(test_result_file):
    l = []
    with open(test_result_file) as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)

    l.remove(l[0])
    label = array(l)
    return to_int(label[:, 1])
