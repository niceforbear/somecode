"""
Author: ykliu
Date: 2019/9/6 00:43
"""

import csv
from numpy import *
from logger import log
from normalizing import normalizing
from utils import to_int


def load_train_data(train_file_path):
    tmp_lines = []

    log("Start load file")
    with open(train_file_path, "r") as f:
        lines = csv.reader(f)
        for line in lines:
            tmp_lines.append(line)

    log("Finish load file")
    tmp_lines.remove(tmp_lines[0])  # drop the first column line

    log("Start trans array")
    tmp_array = array(tmp_lines)
    log("Finish trans array")

    label = tmp_array[:, 0]
    data = tmp_array[:, 1:]

    return normalizing(to_int(data)), to_int(label)


if __name__ == '__main__':
    train_file = "/Users/liuyinkuo/kaggle/digit-recognizer/train.csv"
    load_train_data(train_file)
