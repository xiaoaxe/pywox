#!/usr/bin/env python
# encoding: utf-8

"""
@description: merge pdf

@author: baoqiang
@time: 2021/5/24 8:41 下午
"""

import os
from PyPDF2 import PdfFileMerger
import sys


def merge():
    """
    usage:
        python3 merge_pdf.py $path
    把当前路径下的所有pdf文件合并
    :return:
    """
    target_path = sys.argv[1]
    pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
    pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

    file_merger = PdfFileMerger()
    for pdf in pdf_lst:
        file_merger.append(pdf)  # 合并pdf文件

    output_file = target_path + "/merged.pdf"
    file_merger.write(output_file)
    print(f"success merged file in : {output_file}")

if __name__ == '__main__':
    merge()
