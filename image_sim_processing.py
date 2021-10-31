# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import imagehash ##libraray for similarity ratings in images
from PIL import Image ##image is a library to open images into python
from shutil import copy #imports a functions where you can copy a file in OS
"""
hash0 = imagehash.average_hash(Image.open('../stim/axe_t.jpeg')) 
hash1 = imagehash.average_hash(Image.open('../stim/axe1.png'))
hash2 = imagehash.average_hash(Image.open('../stim/axe2.png')) 
hash3 = imagehash.average_hash(Image.open('../stim/axe3.jpg')) 
hash4 = imagehash.average_hash(Image.open('../stim/axe4.jpg')) 
hash5 = imagehash.average_hash(Image.open('../stim/axe5.jpg'))
hash6 = imagehash.average_hash(Image.open('../stim/axe6.png'))  

print(hash0)
print(hash0-hash1)
print(hash0-hash2)
print(hash0-hash3)
print(hash0-hash4)
print(hash0-hash5)
print(hash0-hash6)
"""
def single_image_proc(base): #def is needed to create a function

    target_imagename = '../proc_stim/'+ base +'_t.png'
    target_image = Image.open(target_imagename)
    target_image = target_image.resize((100,100))
    hash0_diff = imagehash.dhash(target_image)
    hash0_avg = imagehash.average_hash(target_image)
    hash0_perc = imagehash.phash(target_image)
    hash0_wave = imagehash.whash(target_image)
    allimages = [] #made an empty list

    for i in range(1,7):
        imagename = '../proc_stim/'+ base +str(i) + '.png'
        hash_i =  Image.open(imagename) #read in the image
        hash_i = hash_i.resize((100,100)) #resize read images
        hash_idiff = hash0_diff - imagehash.dhash(hash_i)
        hash_iavg = hash0_avg - imagehash.average_hash(hash_i)
        hash_iperc = hash0_perc - imagehash.phash(hash_i)
        hash_iwave = hash0_wave - imagehash.whash(hash_i)
        hash_icomb = ((hash_iavg + hash_idiff + hash_iperc + hash_iwave)/4)
        imagelist = [imagename,hash_icomb]
        allimages.append(imagelist)     #adds items to the list
    """print(hash_icomb, i)    #prints out combined hash score """
    
    sortedlist = sorted(allimages, key = lambda x: x[1]) #sorts in numeric order
    del sortedlist[3:]  #deletes the last 2 item and rating from the list
    sortedlist.insert(0,[target_imagename, 0]) #adds an item to the first place
    
    for image_and_rating in sortedlist: #puts the list into a single column - not sure why to use a for loop
        copy(image_and_rating[0],'../finished_stim') #copies each image set and target to a new folder w. same name
        
        #print(image_and_rating) 


"""
if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')
  """
  