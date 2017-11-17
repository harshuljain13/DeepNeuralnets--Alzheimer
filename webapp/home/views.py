# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

# Create your views here.


def index_view(request):
    if request.method == 'POST':
        return HttpResponse('uploaded')
    if request.method == 'GET':
        return render(request, 'home/index.html')
