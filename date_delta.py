#!/usr/bin/env python
# encoding: utf-8

"""
@description: 计算时间间隔

@author: baoqiang
@time: 2021/5/25 11:29 上午
"""

import sys
from datetime import datetime
import time


def date_delta():
    """
    usage:
        python3 date_delta.py 2021-05-23
    :return:
    """
    time_struct = time.strptime(sys.argv[1], "%Y-%m-%d")
    user_date = datetime.fromtimestamp(time.mktime(time_struct)).date()
    today_date = datetime.now().date()
    delta = user_date - today_date
    print(f'{user_date} away from {today_date}(today) [{delta.days}] days')


if __name__ == '__main__':
    date_delta()
