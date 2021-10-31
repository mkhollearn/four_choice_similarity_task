#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:44:23 2020

@author: martinahollearn
CHECKS FOR TRUNKATED IMAGES IN FINISHED STIM 
"""

from PIL import ImageFile
from PIL import Image
from glob import glob
import os
os.chdir("..")

ImageFile.LOAD_TRUNCATED_IMAGES = False # we want to load in errored out images, that's why it's False

all_fin_images = glob('finished_stim/*.png')

for counter in all_fin_images:
    try:
        counter = Image.open(counter) #make counter = to the all opened images
        counter.load()
        #bad_images.save()
    except:
        print(counter) #if errors out, print the loaded image at each iteration
        
    