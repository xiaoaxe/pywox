#!/usr/bin/env python
# encoding: utf-8

"""
@description: encode base64

@author: baoqiang
@time: 2021/5/27 9:19 下午
"""

import sys
from base64 import b64encode,b64decode


def encode_data():
    """
    usage:
        python3 base64_encode.py d/e 你好
    :return:
    """
    type_ = sys.argv[1]
    data = sys.argv[2]
    if type_ == 'e':
        encoded = b64encode(data.encode('utf-8'))
        print(f'base64 : {data} => {encoded.decode()}')
    elif type_ == 'd':
        decoded = b64decode(data.encode('utf-8'))
        print(f'base64 : {data} => {decoded.decode()}')


if __name__ == '__main__':
    encode_data()
