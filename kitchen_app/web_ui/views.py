# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'floor_options': range(2,15),
    }
    return render(request, 'index.html', context)
