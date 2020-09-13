#!/usr/bin/env python
# encoding: utf-8
'''
@author: cts
@license: Study Only
@contact: hongzuoChu@gmail.com
@software: Pycharm
@file: same_length.py
@time: 2020/9/14 2:23 上午
@desc:
'''

import numpy as np


def list_2_same_len(*args):
    len_args = {len(i) for i in args}
    if len(len_args) != 1:
        for i in args:
            while len(i) != max(len_args):
                i.append(np.nan)


if __name__ == '__main__':
    a = [2, 34, 5, 4, 6]
    b = [1, 3]
    c = [2, 3, 4]
    list_2_same_len(a, b, c)
    print(a, b, c)
