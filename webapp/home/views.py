# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import videoclassification as vc


def index_view(request):
    if request.method == 'POST':
        filename = request.FILES['niifile'].name

        return render(request, 'home/index.html', {'filename': filename})
    if request.method == 'GET':
        return render(request, 'home/index.html')
