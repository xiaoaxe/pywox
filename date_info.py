#!/usr/bin/env python
# encoding: utf-8

"""
@description: 获取日期信息

@author: baoqiang
@time: 2021/5/25 1:09 下午
"""

import sys
import time
from datetime import datetime


def get_date_info():
    """
    usage:
        python3 date_info.py 2021-05-24
    :return:
    """
    time_struct = time.strptime(sys.argv[1], "%Y-%m-%d")
    user_date = datetime.fromtimestamp(time.mktime(time_struct))
    print(f'{user_date} info: week:{user_date.isoweekday()}, timezone: {user_date.astimezone()}')


if __name__ == '__main__':
    get_date_info()
