from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D,TimeDistributed, LSTM, Conv3D
from keras.applications import VGG16
from keras import backend as K
from keras import regularizers
from sklearn.preprocessing import OneHotEncoder
import os
import numpy as np
import nibabel as nib # to read nii files
import shutil # for file operations
import glob  # use to make file list from diectory
import matplotlib.pyplot as plt
import cv2 # opencv library
import matplotlib.image as mpimg
import random
from sklearn.model_selection import train_test_split 
import traceback
import sys
import keras
from gen import DataGenerator

classes = ['Alzheimer',"MCI", 'Normal']
# Declaring the home variables that will be used throughout the script.

home_files_dir = '/home/ubuntu/Select_original_fmri/'
#output_dir='/home/ubuntu/final_src/DeepNeuralnets--Alzheimer/videoclassification/'


train_list=[]
test_list=[]
file_list=[]

for class_ in classes:
    print ('working on ' + class_ + '...')
    
    for root, dir ,files in os.walk(os.path.join('output_array', class_)): 
        length=len(files)
        print("root: ",root)
        if class_ == 'Alzheimer': 
            for file_ in files:            
                npy = np.load(root+'/'+file_)
                if npy.shape == (64, 64, 6720): 
                    file_list.append((npy,0))
            #image data division
            test_list=file_list[:int(length*0.2)]
            train_list=file_list[len(test_list):]
                 
                
        elif class_ == 'MCI':
            len2=len(file_list)
            for file_ in files[:25]:            
                npy = np.load(root+'/'+file_)
                if npy.shape == (64, 64, 6720): 
                    file_list.append((npy,1))
            #image  data  diision
            test_list +=file_list[len2:int(len2+length*0.2)]
            train_list += file_list[int(len2+length*0.2):]
           
            
        # for Normal Class
        
        else:
            len3=len(file_list)
            for file_ in files:            
                npy = np.load(root+'/'+file_)
                if npy.shape == (64, 64, 6720): 
                    file_list.append((npy,2))
            #image  data  diision
            test_list += file_list[len3:int(len3+length*0.2)]
            train_list += file_list[int(len3+length*0.2):]
            
#print ("length of train list: ",len(train_list))
#print("length of train labels:",len(train_labels))
#print("length of test list:",len(test_list))
#print("length of test labels:",len(test_labels))
np.random.shuffle(train_list)
np.random.shuffle(test_list)
X_train,Y_train=zip(*train_list)
X_test,Y_test=zip(*test_list)

#X_train=np.array(X_train,dtype=np.uint8)
#Y_train=np.array(Y_train,dtype=np.uint8)
#X_test=np.array(X_test,dtype=np.uint8)
#print X_test.shape
#Y_test=np.array(Y_test,dtype=np.uint8)
X_test = np.transpose(X_test, [0, 3, 2, 1])
#print X_train.shape
#X_train = np.transpose(X_train, [0, 3, 2, 1])

#for i in X_train:
    
#    print("X train shape: ",i.shape)
#print("Y label shape: ",Y_train.shape)
#print("X test shape: ",X_test.shape)
#print("Y test label: ",Y_test.shape)
#print('done...')
       
# Parameters
params = {'dim_x': 6720,
          'dim_y': 64,
          'dim_z': 64,
          'batch_size': 1,
          'shuffle': True}

training_generator = DataGenerator(**params).generate(Y_train, X_train)
validation_generator = DataGenerator(**params).generate(Y_test, X_test)
                 

batch_size = 1
input_shape = [6720, 64,64]
#Y_train= np_utils.to_categorical(Y_train, num_classes=3)
#Y_test= np_utils.to_categorical(Y_test, num_classes=3)
#np.random.shuffle(data)
#print(X_train.shape)
#print(Y_train.shape)
#print(X_test.shape)
#print(Y_test.shape)
#del(train_list)
#del(test_list)
model = Sequential()
model.add(Conv2D(
    32, (3,3), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (3,3), activation='relu'))
model.add(Conv2D(128, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(256, (2,2), activation='relu'))
model.add(Conv2D(256, (2,2), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(32))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))
model.summary()

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
print Y_train
print Y_test
# model.fit(X_train, Y_train,batch_size=batch_size, epochs=100,verbose=1,validation_data=(X_test, Y_test))
# Train model on dataset
model.fit_generator(generator = training_generator,
                    steps_per_epoch = len(X_train)//batch_size,
                    epochs = 2,
                    validation_data = validation_generator,
                    validation_steps = len(X_test)//batch_size)
Y_test= np_utils.to_categorical(Y_test, num_classes=3)
print X_test[0].shape
for i in range(len(X_train)-2):
    print i,i+1
    print model.predict_classes(nX_train[i:i+1])
#score = model.evaluate(X_test, Y_test, verbose=0)
json_string = model.to_json()
with open("arch.json","w") as f:
    f.write(json_string)
model.save_weights("weights.h5")
#print('Test loss:', score[0])
#print('Test accuracy:', score[1])