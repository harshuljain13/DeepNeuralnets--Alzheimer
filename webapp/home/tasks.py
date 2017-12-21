
from celery.decorators import task
import numpy as np
import nibabel as nib
from keras.models import Sequential
import keras
import time

@task(name="predict_nii_file")
def predict_nii_file(filename):
    t1 = time.clock()
    nib.load(os.path.join('../media', filename))
    time_taken = time.clock() - t1
    return time_taken
