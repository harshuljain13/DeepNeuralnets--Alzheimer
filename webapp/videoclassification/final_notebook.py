
# coding: utf-8

# # Video Classification
# 
# This script consists all the steps for video classification.
# 
# 1. extracting the images from the nii files.
# 2. converting the images of the nii file into the video.
# 3. converting the video into images again.
# 4. running extract_features.py to get the features from the vgg.
# 5. running train.py to train the deep neural model.
# 
# 

# In[ ]:


import os
import numpy as np
import nibabel as nib # to read nii files
import shutil # for file operations
import glob  # use to make file list from diectory
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import cv2 # opencv library
import matplotlib.image as mpimg
import random
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score
from skimage import filters
from skimage import measure
from skimage.color import rgb2gray
from skimage.morphology import closing, square
import traceback
import sys

# Declaring the home variables that will be used throughout the script.

classes = ['Alzheimer',"MCI", 'Normal']
home_files_dir = '/home/ubuntu/Select_original_fmri/'

data = []
labels = []

path = "/home/ubuntu/Select_original_fmri/niifiles/"
#dst = "/home/ubuntu/Select_original_fmri/data/"
dst = 'data/'
files_list = [] 
test_list = []
train_list = []

count  = 0

#try:
#    os.mkdir(dst)
#except:
#    shutil.rmtree(dst)
#    os.mkdir(dst)

try:
    os.mkdir(dst+"test/")
    os.mkdir(dst+"train/")
except:
    shutil.rmtree(dst+"test/")
    shutil.rmtree(dst+"train/")
    os.mkdir(dst+"test/")
    os.mkdir(dst+"train/")
    
for class_ in classes:
    print class_
    
    # dividing the data for training and testing purpose
    try:
        os.mkdir(dst+"test/"+class_)
        os.mkdir(dst+"train/"+class_)
    except:
        shutil.rmtree(dst+"train/"+class_)
        shutil.rmtree(dst+"test/"+class_)
        os.mkdir(dst+"test/"+class_)
        os.mkdir(dst+"train/"+class_)
        
    for root,dirs,files in os.walk(os.path.join(path,class_)):
        for f in files:
            files_list.append(f)
        test = int(len(files_list)*.3) # 30% test data
        train = int(round(len(files_list)*.7)) # 70% test data
        test_list += list(files_list[:test])
        train_list += list(files_list[test:train])
        
        #moving data into test and train folders
        for i in test_list:
            shutil.copy(src=path+class_ +"/"+i, dst=dst+"test/"+class_+"/"+i)
        for i in train_list:
            shutil.copy(src=path +  class_ +"/"+ i, dst=dst+"train/" +class_+"/"+i)
        files_list = []
        train_list = []
        test_list  = []


# In[13]:


#get_ipython().magic('cd data')


# In[14]:


#try:
#    os.mkdir("sequences/")
#    os.mkdir("checkpoints/")
#except:
#    shutil.rmtree("sequences/")
#    shutil.rmtree("checkpoints/")
#    os.mkdir("sequences/")
#    os.mkdir("checkpoints/")


# In[39]:


#this is used to extract images
#get_ipython().system('python 2_extract_files.py')


# In[10]:


#get_ipython().magic('cd ..')


# In[7]:


#get_ipython().system('python extract_features.py')


# In[ ]:


#get_ipython().system('python train.py')


# In[ ]:





# In[ ]:





# \begin\{*equation}
# 
# \end\{*equation}

# In[ ]:




