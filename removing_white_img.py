#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:51:18 2020

@author: martinahollearn
"""

## - remove all white and makes it transparent then saves it
from PIL import Image

img = Image.open('../stim/candle6.png')
img = img.convert("RGBA")
datas = img.getdata()
newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img.putdata(newData)
img.save("../proc_stim/candle6.png", "PNG")
img.show()
