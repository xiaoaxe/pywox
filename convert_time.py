#!/usr/bin/env python
# encoding: utf-8

"""
@description: 时间转化

@author: baoqiang
@time: 2021/5/18 4:52 下午
"""

import sys
import time


def convert():
    """
    usage:
        python3 covert_time.py return "current_ts"
        python3 covert_time.py 1621864350 return "time str"
        python3 covert_time.py "2021-05-24 21:52:30" return "ts"
    :return:
    """
    if len(sys.argv) == 2:
        time_str = sys.argv[1]

        try:
            ts = int(time_str)
            ts_local = time.localtime(ts)
            dt_str = time.strftime("%Y-%m-%d %H:%M:%S", ts_local)
            print('{} -> {}'.format(time_str, dt_str))
        except Exception as e:
            dt = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            ts = time.mktime(dt)
            print('{} -> {}'.format(time_str, int(ts)))
    elif len(sys.argv) == 1:
        print(int(time.time()))


if __name__ == '__main__':
    convert()
