#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

s1 = ['soe', 'snis', 'ssni']
ip = ['iptd', 'ipz']
md = ['midd', 'mide', 'miad', 'migd']
ab = ['abp']
oth = ['star', 'pgd', 'rbd', 'shkd', 'ebod', 'mxgs', 'wanz', 'dasd']

going = {
    'ssis': 267,
    'ipx': 786,
    'midv': 111,
    'abw': 178,
    'fsdss': 321,
    'stars': 466,
    'miaa': 545,
    'atid': 462,
}


def get_one():
    '''
    total len: 13126
    '''
    candidate = []

    list = s1+ip+md+ab
    for pre in list:
        for i in range(1, 1000):
            candidate.append(f'{pre}-{i:03d}')

    for pre, cnt in going.items():
        for i in range(1, cnt+1):
            candidate.append(f'{pre}-{i:03d}')

    print(f'total len: {len(candidate)}')
    lucky = random.sample(candidate, 5)
    print('lucky:\n', '\n'.join(lucky), sep='')


if __name__ == '__main__':
    get_one()
