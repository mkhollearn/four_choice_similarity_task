#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 12:04:42 2020

@author: martinahollearn

PROCESSES ALL IMAGES FROM PROC STIM AND PUTS THE SELECTED IMAGES TO FINISHED_STIM
"""


#create a function where we can sub in any image name for 'base' in image_sim_processing script

from image_sim_processing import single_image_proc
from glob import glob
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

#single_image_proc("banana") #need to import it as str to use it in the path, otherwise it records as variable

all_image_names = glob('../proc_stim/*_t.png')
path = '../proc_stim'
src_dir = '../raw_stim'
dest_dir = '../proc_stim'

for single_image_name in all_image_names: #my i here = single_image_name bc it is more helpful to know what i is here
    try: 
       
       single_image_name = single_image_name[13:]
       single_image_name = single_image_name[:-6]
       single_image_proc(single_image_name) #this is my function
       #print(single_image_name)
    except Exception as error :  #Exception is the error called in python, it prints out what is the error
            print('There was an error with ' + single_image_name)
            print(error)
      
                
'''    
test = "../proc_stim/dustpan_t.png"
try:

    test = test[13:]
    test = test[:-6]
    print(test) 
    single_image_proc(test)
except: 
    print('There was an error with ' + test)
'''    
    
    