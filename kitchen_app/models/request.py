# -*- coding: utf-8 -*-
from django.db import models


from employee import Employee
from item import Item


class Request(models.Model):
    requester = models.ForeignKey(Employee)
    request_time = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item)
    status = models.PositiveSmallIntegerField(default=0)
    employee_location = models.CharField(max_length=200, default='Unspecified')

    class Meta:
        db_table = 'request'
