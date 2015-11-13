# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from kitchen_app.models.item import Item

def index(request):
    context = {
        'floor_options': range(2,15),
        'items': [item.name for item in Item.objects.all()]
    }
    return render(request, 'index.html', context)
