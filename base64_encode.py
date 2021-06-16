#!/usr/bin/env python
# encoding: utf-8

"""
@description: encode base64

@author: baoqiang
@time: 2021/5/27 9:19 下午
"""

import sys
from base64 import b64encode


def encode_data():
    """
    usage:
        python3 base64_encode.py 你好
    :return:
    """
    data = sys.argv[1]
    encoded = b64encode(data.encode('utf-8'))
    print(f'base64 encoded: {data} => {encoded}')


if __name__ == '__main__':
    encode_data()
