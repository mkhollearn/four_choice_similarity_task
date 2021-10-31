#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:59:37 2020

@author: martinahollearn

#PRINTS THE GRAND LIST FOR PAVLOVIA
"""
from glob import glob
import os 
from PIL import ImageFile


os.chdir("..") #changed out one directory into the SocialMDTbias folder
ImageFile.LOAD_TRUNCATED_IMAGES = True

grand_list = []

all_target_image_names = glob('finished_stim/*_t.png') #path changed to the finished images
# star represents any number of characters and here how base_name and * are compatible is the orer the code runs them in

for target_image_name in all_target_image_names: #my i here = single_image_name bc it is more helpful to know what i is here
       
    
        one_stim_list = []
        base_name = target_image_name[14:]
        base_name = base_name[:-6]
        lure_image_names = glob('finished_stim/' + base_name + '?.png') #? means 1 single character in bash
        one_stim_list.append(target_image_name)
        grand_list.append(one_stim_list + lure_image_names) #adding two lists together bc lure_image names is already a list of 3 items
        #print(base_name) #to check if i chopped down the base name properly
        #print(all_lure_image_names) #returns the path plus all images _t.png
        #print(grand_list)

for one_stim_list in grand_list: #organizes your list within the list into a new row for each sublist
    print(one_stim_list, ",") #print function always prints to a new line
    