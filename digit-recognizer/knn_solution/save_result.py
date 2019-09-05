"""
Author: ykliu
Date: 2019/9/6 01:42
"""


def save_result(result, result_file):
    with open(result_file, 'w') as myFile:
        for idx in range(len(result)):
            myFile.write("{},{}\n".format(idx+1, result[idx]))
