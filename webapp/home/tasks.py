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
    current_task.update_state(state='PROGRESS', meta={'process_percent':30})
    x = nib.load(os.path.join('media', filename)).get_data()
    #time.sleep(30)
    return 'DONE'

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
        process_percent = 100
    if status == 'PROGRESS':
        process_percent = task.info['process_percent']
    return {'status':status, 'process_percent':process_percent}
