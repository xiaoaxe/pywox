#!/usr/bin/env python
# encoding: utf-8

"""
@description: 生成md5

@author: baoqiang
@time: 2021/6/1 9:15 下午
"""

import hashlib
import sys
import os


def gen_md5():
    """
    usage:
        python3 sum_md5.py 'hello, world, 你好'
        python3 sum_md5.py '${file_name}'
    :return:
    """
    data_or_file = sys.argv[1]
    if os.path.isfile(data_or_file):
        with open(data_or_file, 'r') as f:
            data = f.read()
    else:
        data = data_or_file

    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    print(f'data {data} get md5 sum is: {m.hexdigest()}')


if __name__ == '__main__':
    gen_md5()
