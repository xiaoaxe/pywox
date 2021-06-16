#!/usr/bin/env python
# encoding: utf-8

"""
@description: 随机一个数据

@author: baoqiang
@time: 2021/5/27 9:26 下午
"""

import sys
import random


def random_one():
    """
    usage:
        python3 lucky.py 'dog cat'
    :return:
    """
    data_str = sys.argv[1]
    datas = data_str.split(' ')
    if ',' in data_str:
        datas = data_str.split(',')
    lucky = random.sample(datas, 1)
    print(f'"{data_str}" get lucky: {lucky[0]}')


if __name__ == '__main__':
    random_one()
