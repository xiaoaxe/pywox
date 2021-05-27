#!/usr/bin/env python
# encoding: utf-8

"""
@description: 转化成农历

@author: baoqiang
@time: 2021/5/25 1:02 下午
"""

from zhdate import ZhDate
import sys
import time
from datetime import datetime


def covert():
    """
    usage:
        python3 convert_lunar.py 2021-05-25
    :return:
    """
    time_struct = time.strptime(sys.argv[1], "%Y-%m-%d")
    user_date = datetime.fromtimestamp(time.mktime(time_struct))
    lunar_date = ZhDate.from_datetime(user_date)
    print(f'{user_date.date()} is chinese lunar: {lunar_date.chinese()}')


if __name__ == '__main__':
    covert()
