#!/usr/bin/env python
# encoding: utf-8

"""
@description: 把image合并为pdf

@author: baoqiang
@time: 2021/6/16 10:14 下午
"""

from fpdf import FPDF
import sys
import os


def save_images():
    """
    usaeg:
        python3 save_img.py ${file_name}
    :return:
    """
    path = sys.argv[1]

    pdf = FPDF()
    pdf.add_page()

    for file in os.listdir(path):
        if '.DS_Store' == file:
            continue
        image_file = os.path.join(path, file)
        pdf.image(image_file)

    output_file = os.path.join(os.environ['HOME'], "images.pdf")
    pdf.output(output_file, 'F')

    print(f"success saved pdf file in : {output_file}")


if __name__ == '__main__':
    save_images()
