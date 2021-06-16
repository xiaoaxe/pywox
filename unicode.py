#!/usr/bin/env python
# encoding: utf-8

"""
@description: 转化成unicode

@author: baoqiang
@time: 2021/5/27 9:31 下午
"""

import sys
# from binascii import unhexlify, hexlify
from binascii import a2b_hex

codings = [
    'utf-8',
    'gbk',
    'unicode_escape'
]


def to_unicode():
    """
    usage:
        python3 unicode.py '\xe5\xb0\x8f\xe5\x8c\x85'
        python3 unicode.py '\\xd0\\Xa1\xb0\Xfc'
        python3 unicode.py '\\u5c0f\u5305'
    :return:
    """
    origin = sys.argv[1]
    data_str = origin

    data_str = data_str.replace('U', 'u')
    if r'\u' in data_str:
        for symbol in [r'\\u']:
            data_str = data_str.replace(symbol, r'\u')
        decoded = data_str.encode('latin-1').decode('unicode-escape')
        print(f'{origin} decode to {decoded} with coding unicode-escape')
        return

    data_str = data_str.replace('X', 'x')
    for symbol in [r'\\x', r'\x']:
        if symbol in data_str:
            data_str = data_str.replace(symbol, '')

    for coding in codings:
        try:
            decoded = a2b_hex(data_str).decode(coding)
            print(f'{origin} decode to {decoded} with coding {coding}')
            return
        except Exception as e:
            print(e)
            pass

    print(f'invalid input: {data_str}')


if __name__ == '__main__':
    to_unicode()
