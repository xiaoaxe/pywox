#!/usr/bin/env python
# encoding: utf-8

"""
@description: uuid

@author: baoqiang
@time: 2021/6/16 10:05 下午
"""

import sys
import uuid

name = 'hello'


def gen_uuid():
    """
        python3 gen_uuid.py
    :return:
    """
    uuid1 = uuid.uuid1()
    uuid3 = uuid.uuid3(uuid.NAMESPACE_DNS, name)  # base md5
    uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, name)  # base sha1

    print(f'uuid1: {uuid1}, uuid3: {uuid3}, uuid5: {uuid5}')


if __name__ == '__main__':
    gen_uuid()
