#!/usr/bin/env python
# encoding: utf-8

"""
@description: jwt生成

@author: baoqiang
@time: 2021/5/28 12:53 下午
"""

import jwt
import sys
import json

secret = 'your unique secret'
alg = 'HS256'


def gen():
    """
    usage:
        python3 gen_jwt.py '{"user_id": 123}'
        python3 gen_jwt.py 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjN9.BFiy42ZY2PAC_TXZ77Bl9l69bjLt1UkMRcWG_LwNf48'
    :return:
    """
    data = sys.argv[1]
    try:
        jdata = json.loads(data)
        encoded = jwt.encode(payload=jdata, key=secret, algorithm=alg)
        print(f'{data} encoded to jwt token: {encoded}')
    except Exception as e:
        decoded = jwt.decode(jwt=data, key=secret, algorithms=alg)
        print(f'{data} decoded to jwt token: {decoded}')


if __name__ == '__main__':
    gen()
