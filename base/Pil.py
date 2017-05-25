#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_

'a Python Image Libary Test model'

__author__='linguanghui'

from PIL import Image

im = Image.open('test.png')

print(im.format, im.size, im.mode)

