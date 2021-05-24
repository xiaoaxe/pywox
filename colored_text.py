#!/usr/bin/env python
# encoding: utf-8

"""
@description: 打印颜色

@author: baoqiang
@time: 2021/5/24 9:37 下午
"""

from sty import fg, bg, Style, RgbFg
import sys


def colored():
    """
    usage:
        python3 colored_text.py 255,0,0
        python3 colored_text.py '#FF0000'
    :return:
    """
    rgb = sys.argv[1]
    rgbs = rgb.split(',')
    if len(rgbs) == 3:
        r, g, b = rgbs
    elif rgb.startswith('#') and len(rgb) == 7:
        rgb = rgb[1:]
        r, g, b = int(rgb[0:2], 16), int(rgb[2:4], 16), int(rgb[4:6], 16)
    else:
        raise Exception(f'invalid input: {rgb}')

    fg.color = Style(RgbFg(r, g, b))
    print(fg.color + "text", fg.rs)


if __name__ == '__main__':
    colored()
