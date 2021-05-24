#!/usr/bin/env python
# encoding: utf-8

"""
@description: 下载文件

@author: baoqiang
@time: 2021/5/24 10:01 下午
"""

import requests
import sys
import os
import time

allowed_files = ['pdf', 'png', 'jpeg', 'jpg']


def download():
    """
    usage:
        python3 download_file.py 'https://www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png'
    :return:
    """
    url = sys.argv[1]

    suffix = url.split('.')[-1]
    if suffix not in allowed_files:
        raise Exception(f'not allowed suffix: {suffix}')

    try:
        output_file = sys.argv[2]
    except Exception as e:
        filename = url.split('/')[-1]
        output_file = os.environ["HOME"] + f"/{filename}"

    resp = requests.get(url)
    with open(output_file, 'wb') as fw:
        fw.write(resp.content)

    print(f"success saved download file in : {output_file}")


if __name__ == '__main__':
    download()
