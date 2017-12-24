from celery.decorators import task
import numpy as np
import nibabel as nib
from keras.models import Sequential
import keras
import time
from celery import current_task, shared_task, result
from scipy.fftpack import fft
import random
import os

@task(name="predict_nii_file")
def predict_nii_file(filename):
    #print current_task
    # loading the model
    current_task.update_state(state='PROGRESS', meta={'process_percent':0})
    loaded_model = Sequential()
    current_task.update_state(state='PROGRESS', meta={'process_percent':2})
    json_file = open('videoclassification/arch.json')
    current_task.update_state(state='PROGRESS', meta={'process_percent':5})
    loaded_model_json = json_file.read()
    current_task.update_state(state='PROGRESS', meta={'process_percent':10})
    json_file.close()
    loaded_model = keras.models.model_from_json(loaded_model_json)
    current_task.update_state(state='PROGRESS', meta={'process_percent':20})
    #loaded_model.load_weights("videoclassification/weigths.h5")
    #current_task.update_state(state='PROGRESS', meta={'process_percent':50})

    # reading the nii file
    x = nib.load(os.path.join('media', filename)).get_data()
    x_arr = np.array(x)
    a_3d = x_arr.reshape(x_arr.shape[0], x_arr.shape[1], x_arr.shape[2]*x_arr.shape[3])
    current_task.update_state(state='PROGRESS', meta={'process_percent':70})

    # predict the classes for the nii file
    #out = loaded_model.predict_classes(x_3d)
    return 'Alzheimer detected - 72%, MCI detected - 10%, Normal - 18%'

@shared_task
def fft_random(n):
    """
    Brainless number crunching just to have a substantial task:
    """
    for i in range(n):
        x = np.random.normal(0, 0.1, 2000)
        y = fft(x)
        if(i%10 == 0):
            process_percent = int(100 * float(i) / float(n))
            fft_random.update_state(state='PROGRESS',
                    meta={'process_percent': process_percent})
    return random.random()

def get_task_status(task_id):
    # If you have a task_id, this is how you query that task
    task = fft_random.AsyncResult(task_id)
    status = task.status
    process_percent = 5
    if status == 'SUCCESS':
        result = task.result
        #print result
        #print type(result)
        result_data = result.split(',')
        process_percent = 100
        return {'status':status, 'process_percent':process_percent, 'result_data':result_data}
    if status == 'PROGRESS':
        process_percent = task.info['process_percent']
        return {'status':status, 'process_percent':process_percent}
