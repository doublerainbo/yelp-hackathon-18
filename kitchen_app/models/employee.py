# -*- coding: utf-8 -*-
from django.db import models


class Employee(models.Model):
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    username = models.CharField(max_length=32)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        db_table = 'employee'
