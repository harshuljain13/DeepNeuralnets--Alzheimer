# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from .tasks import *
import json


def index_view(request):
    if request.method == 'POST':
        file_ = request.FILES['niifile']
        fs = FileSystemStorage()
        new_filename = fs.save(file_.name, file_)
        task = predict_nii_file.delay(new_filename)
        #task = fft_random.delay(100000)
        return render(request,'home/index.html',{'filename':new_filename, 'task_id':task.id})
    if request.method == 'GET':
        return render(request, 'home/index.html')

def poll_state(request):
    status_data='Fail'
    if request.is_ajax():
        if 'task_id' in request.POST.keys() and request.POST['task_id']:
            task_id = request.POST['task_id']
            status_data = get_task_status(task_id)
        else:
            status_data = 'No task_id in the request'
    else:
        status_data = 'This is not ajax request'

    json_data = json.dumps(status_data)
    print json_data
    return HttpResponse(json_data, content_type='application/json')
