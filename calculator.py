#!/usr/bin/env python
# encoding: utf-8

"""
@description: 计算器

@author: baoqiang
@time: 2021/5/27 9:08 下午
"""

import sys


def calculate():
    """
    usage:
        python3 calculator.py '1+2*(3+4)'
    :return:
    """
    expr = sys.argv[1]
    res = eval(expr)
    print(f"calculate {expr}={res}")


if __name__ == '__main__':
    calculate()
