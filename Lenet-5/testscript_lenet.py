import os
import numpy as np
import nibabel as nib
import glob
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import cv2
import matplotlib.image as mpimg
import random
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score
from skimage import filters
from skimage import measure
from skimage.color import rgb2gray
from skimage.morphology import closing, square
import shutil
from os import listdir
from os.path import isfile, join
import pandas as pd

dataset_name = 'Norm-Alz'
home_files_dir2 = '/home/ubuntu/testing/niifiles/'
os.mkdir('/home/ubuntu/'+dataset_name+'/processed/test_64/')

filename_list = []
perc_alz_list = []
perc_mci_list = []
perc_normal_list = []

for file_ in listdir(home_files_dir2):
    if isfile(join(home_files_dir2,file_)):
        x = nib.load(join(home_files_dir2, file_)).get_data()
        shutil.rmtree('/home/ubuntu/'+dataset_name+'/processed/test_64/')
        os.mkdir('/home/ubuntu/'+dataset_name+'/processed/test_64/')
        count=1
        for i in xrange(x.shape[3]):
            for j in xrange(x.shape[2]):
                if j > 25 and j < 75:
                    continue
                else:
                    y = x[:, :, j, i] 
                    img = Image.fromarray(y)
                    img = img.convert("RGB")
                    img = img.resize([64, 64])
                    img.save('/home/ubuntu/'+dataset_name+'/processed/test_64/i_' + str(count) + ".jpg")
                    count+=1
	os.system('python -m tefla.predict --model examples/DeepNeuralnets--Alzheimer/Lenet-5/model_train.py \
	--training_cnf examples/DeepNeuralnets--Alzheimer/Lenet-5/train_cnf.py \
	--predict_dir ../../Norm-Alz/processed/test_64/ --predict_type 1_crop --weights_from weights/model-epoch-15.ckpt')
	
	df = pd.read_csv('/home/ubuntu/'+dataset_name+'/processed/predictions/results/predictions_class.csv')
	alz_count = float(df[df['label']==0]['label'].count())
	#alz_count=0
	#MCI_count = float(df[df['label']==1]['label'].count())
	MCI_count=0
	Normal_count = float(df[df['label']==1]['label'].count())
	#Normal_count=0
	total_count = alz_count + MCI_count + Normal_count
	perc_alz = (alz_count/total_count)*100
	perc_mci = (MCI_count/total_count)*100
	perc_normal = (Normal_count/total_count)*100
	filename_list.append(file_)
	perc_alz_list.append(perc_alz)
	perc_mci_list.append(perc_mci)
	perc_normal_list.append(perc_normal)


df2 = pd.DataFrame({'filename':filename_list, 'perc_alz':perc_alz_list, 'perc_MCI':perc_mci_list, 'perc_Normal':perc_normal_list})
df2.to_csv('/home/ubuntu/'+dataset_name+'/results.csv')
