#!/usr/bin/env python
# encoding: utf-8

"""
@description: todo

@author: baoqiang
@time: 2021/5/24 8:49 下午
"""
import pyqrcode
import os
import sys
import png


def gen():
    """
    usage:
        python3 gen_qrcode.py https:www.baidu.com [output_path]
    :return:
    """
    data = sys.argv[1]
    try:
        outfile = sys.argv[2]
    except Exception as e:
        outfile = os.environ["HOME"] + f"/{data}.png"
    url = pyqrcode.create(data)
    # url.show()
    url.png(outfile, scale=6)
    print(f"success saved qrcode png file in : {outfile}")


if __name__ == '__main__':
    gen()
