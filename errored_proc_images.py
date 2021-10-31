#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:11:52 2020

@author: martinahollearn
CHECKS TRUNKATED IMAGES IN ALL PROC STIM
"""


from PIL import ImageFile
from PIL import Image
from glob import glob
import os
os.chdir("..")

ImageFile.LOAD_TRUNCATED_IMAGES = False # we want to load in errored out images, that's why it's False

all_proc_images = glob('proc_stim/*.png')

for counter in all_proc_images:
    try:
        counter = Image.open(counter) #make counter = to the all opened images
        counter.load()
        #bad_images.save()
    except:
        print(counter) #if errors out, print the loaded image at each iteration