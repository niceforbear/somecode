"""
Author: ykliu
Date: 2019/9/6 02:31
"""

label_file = "/Users/liuyinkuo/kaggle/digit-recognizer/knn_benchmark.csv"
result_file = "{}.result.csv".format(label_file)
with open(label_file, 'r') as f:
    lines = f.readlines()

with open(result_file, 'w') as f:
    f.write("ImageId,Label\n")
    for idx in range(len(lines)):
        f.write("{},{}".format(idx+1, lines[idx]))
