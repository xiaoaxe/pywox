#!/usr/bin/env python
# encoding: utf-8

"""
@description: 格式化json

@author: baoqiang
@time: 2021/5/25 12:45 下午
"""

import sys
from pprint import pprint
import os
import json


def format_json():
    """
    usage:
        python3 format_json.py '{"name": "xiao", "age": 18}'
        python3 format_json.py ${file_name}
        :same as jq command:
    :return:
    """
    file_or_data = sys.argv[1]
    if os.path.isfile(file_or_data):
        with open(file_or_data, 'r') as f:
            data = f.read()
    else:
        data = file_or_data
    jdata = json.loads(data)
    fdata = json.dumps(jdata, indent=4, sort_keys=True, ensure_ascii=False)
    print(fdata)


if __name__ == '__main__':
    format_json()
