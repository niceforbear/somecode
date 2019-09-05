"""
Author: ykliu
Date: 2019/9/6 00:39
"""

from load_train_data import load_train_data
from load_test_data import *
from numpy import shape
from knn import knn
from logger import log
from save_result import save_result


def digit_recognizer(train_data_file, test_data_file, test_label_file, test_result_file, knn_k):
    log("Start get train data & label.")
    train_data, train_label = load_train_data(train_data_file)

    log("Start get test data.")
    test_data = load_test_data(test_data_file)

    log("Start get test label.")
    test_label = load_test_result(test_label_file)
    log("test label: {}".format(test_label))
    m, n = shape(test_data)
    error_count = 0
    result = []
    for idx in range(m):
        log("main iter: {}".format(idx))
        classifier_result = knn(test_data[idx], train_data, train_label, knn_k)
        result.append(classifier_result)
        log("the class result: {}, the true answer: {}".format(classifier_result, test_label[0, idx]))
        if classifier_result != test_label[0, idx]:
            error_count += 1

    log("error count: {}".format(error_count))
    log("error rate: {}".format(error_count / float(m)))

    save_result(result, test_result_file)


if __name__ == "__main__":
    train_file = "/Users/liuyinkuo/kaggle/digit-recognizer/train_v2.csv"
    test_file = "/Users/liuyinkuo/kaggle/digit-recognizer/test_v2.csv"
    test_label_file = "/Users/liuyinkuo/kaggle/digit-recognizer/knn_benchmark.csv.result.csv.v2.csv"
    result_file = "./result.csv"
    digit_recognizer(train_file, test_file, test_label_file, result_file, 10)
