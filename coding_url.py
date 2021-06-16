#!/usr/bin/env python
# encoding: utf-8

"""
@description: url编解码

@author: baoqiang
@time: 2021/5/27 9:15 下午
"""

import sys
from urllib.parse import quote, unquote


def encode_or_decode_url():
    """
    usage:
        python3 coding_url.py 'https://www.baidu.com/s?wd=北京'
    :return:
    """
    url = sys.argv[1]
    if '%' not in url:
        encoded = quote(url)
        print(f'url encode: {url} => {encoded}')
    else:
        decoded = unquote(url)
        print(f'url decode: {url} => {decoded}')


if __name__ == '__main__':
    encode_or_decode_url()
