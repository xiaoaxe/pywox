#!/usr/bin/env python
# encoding: utf-8

"""
@description: md文件转成pdf

@author: baoqiang
@time: 2021/6/17 8:55 下午
"""

import sys
import subprocess
import os
import pathlib


# npm i -g md-to-pdf
# image: python3 -m http.server serve http files or md image file path use local relative path
# // brew install pandoc
# // brew install basictex
def save_md():
    """
    usage:
        python3 save_md.py ${md_file} ${img_base_url}
    :return:
    """
    md_file = sys.argv[1]
    # output_file = os.path.join(os.environ['HOME'], 'output.pdf')
    p = subprocess.Popen(f'md2pdf {md_file}', shell=True)
    p.wait()

    file_path = pathlib.Path(md_file).parent
    print(f"success saved pdf file in : {file_path}")


if __name__ == '__main__':
    save_md()
