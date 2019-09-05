"""
Author: ykliu
Date: 2019/9/6 01:10
"""

from numpy import matrix, tile, array
import operator
from logger import log

DEFAULT_KNN_K = 10


def knn(in_x, train_data, label_data, knn_k=DEFAULT_KNN_K):
    in_x = matrix(in_x)
    train_data = matrix(train_data)
    labels = matrix(label_data)
    # log('labels: {}'.format(labels))
    train_data_size = train_data.shape[0]

    # log("in_x shape: {}, train data shape: {}".format(in_x.shape, train_data.shape))
    diff_mat = tile(in_x, (train_data_size, 1)) - train_data
    # log('diff mat: {}'.format(diff_mat))

    sq_diff_mat = array(diff_mat) ** 2
    # log('sq diff mat: {}'.format(sq_diff_mat))

    sq_distances = sq_diff_mat.sum(axis=1)
    # log('sq dist: {}'.format(sq_distances))

    distances = sq_distances ** 0.5
    # log('dist: {}'.format(distances))

    sorted_dist_indices = distances.argsort()
    # log('sorted_dist_indices: {}'.format(sorted_dist_indices))

    class_count = {}
    for i in range(knn_k):
        # log("Knn iter: {}".format(i))
        vote_i_label = labels[0, sorted_dist_indices[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1
        # log('class count vote i label: {}'.format(class_count[vote_i_label]))

    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    # log('sorted class count: {}'.format(sorted_class_count))
    return sorted_class_count[0][0]


if __name__ == "__main__":
    test_in_x = [0, 1]
    test_train_data = [[0, 1], [1, 0], [1, 0], [0, 1], [0, 1], [0, 1], [0, 1], [1, 0]]
    test_label_data = [0, 1, 1, 0, 0, 0, 0, 1]
    test_k = 8
    res = knn(test_in_x, test_train_data, test_label_data, test_k)
    log(res)
