#!/usr/bin/env python
# encoding: utf-8

"""
@description: 格式化日期

@author: baoqiang
@time: 2021/5/27 8:43 下午
"""

import sys
import time
from datetime import datetime

date_fmts = [
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%d %H:%M',
    '%y-%m-%d %H:%M:%S',
    '%y-%m-%d %H:%M',
    '%Y-%m-%d',
    '%y-%m-%d',
    '%H:%M:%S',
    '%H:%M',
    '%Y%m%d %H:%M:%S',
    '%Y%m%d %H:%M',
    '%y%m%d %H:%M:%S',
    '%y%m%d %H:%M',
    '%Y%m%d',
    '%y%m%d',
]


def format_date():
    """
    usage:
        python3 format_date.py '2021-05-27 08:01:02'
    :return:
    """
    dt_str = sys.argv[1]
    for fmt in date_fmts:
        try:
            tm_struct = time.strptime(dt_str, fmt)
            dt = datetime.fromtimestamp(time.mktime(tm_struct))
            if fmt.startswith('%H'):
                dt = datetime.combine(datetime.now().date(), dt.time())
            print(f'input time: {dt_str} iso8601 time format: {dt.isoformat()}')
            return
        except Exception as e:
            pass

    print(f"invalid input: {dt_str}")


if __name__ == '__main__':
    format_date()
