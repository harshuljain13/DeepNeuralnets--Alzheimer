# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from .tasks import predict_nii_file

def index_view(request):
    if request.method == 'POST':
        file_ = request.FILES['niifile']
        fs = FileSystemStorage()
        new_filename = fs.save(file_.name, file_)
        time_taken = predict_nii_file.delay(new_filename)
        return render(request, 'home/index.html', {'filename': new_filename, 'time_take':time_taken})
    if request.method == 'GET':
        return render(request, 'home/index.html')
