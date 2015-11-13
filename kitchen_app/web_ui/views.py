# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from kitchen_app.models.item import Item
from kitchen_app.models.request import Request


def index(request):
    context = {
        'floor_options': range(2,15),
        'items': [(item.id, item.name) for item in Item.objects.all()],
        'active_requests': [(r.id, r.item.item.name, r.requester.full_name, r.employee_location) for r in Request.objects.filter(status=0)],
    }
    return render(request, 'index.html', context)
