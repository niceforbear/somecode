"""
Author: ykliu
Date: 2019/9/6 00:45
"""

import logging
import time

logging.basicConfig(level=logging.INFO)


def log(msg, level=logging.INFO):
    now = time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
    msg = "{}: {}".format(now, msg)
    logging.log(level, msg)


if __name__ == "__main__":
    log("test", logging.INFO)
    log("test")
    log("test", logging.ERROR)
