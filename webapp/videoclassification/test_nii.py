import os
import numpy as np
import nibabel as nib # to read nii files
import shutil # for file operations
import glob
from keras.models import Sequential
import keras

# Declaring the home variables that will be used throughout the script.

home_files_dir = '/home/ubuntu/Select_original_fmri/'
#output_dir='/home/ubuntu/final_src/DeepNeuralnets--Alzheimer/videoclassification/'

loaded_model = Sequential()
# load json and create model
json_file = open('arch.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = keras.models.model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("weights.h5")
nii_file=[]


#removing existing "output_array" (old data) folder from the directory '/home/ubuntu/Select_original_fmri/images
# iterating /home/ubuntu/Select_original_fmri/niifiles/class_ 
classes=("Alzheimer", "MCI" , "Normal")
for class_ in classes:
    print ('working on ' + class_ + '...')
    
    for root, dir ,files in os.walk(os.path.join(home_files_dir+"niifiles/" , class_)): 
        
        count = 0
        for file_ in files:
            #print 'working on ' + file_ + '...'
            #try:
                # extracting data from nii files
                x = nib.load(os.path.join(home_files_dir+"niifiles/" , class_) + '/' + file_).get_data()
                print("x_shape",x.shape)
                x_arr=np.array(x)
                #print ("x_arr shape : ",x_arr.shape)
                #converting X_arr into 3_D array.........
                x_3d = x_arr.reshape(x_arr.shape[0],x_arr.shape[1],x_arr.shape[2]*x_arr.shape[3])
                out=loaded_model.predict_classes(x_3d)
                print out
                #np.save('output_array' +'/'+ class_ + '/'+str(file_)+str(count),x_3d)
                count+=1
                #print("3d array shape : ",x_3d.shape)
                break
            #except:
                print("in last except block")
                print file_
                break

