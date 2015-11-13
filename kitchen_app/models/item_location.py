# -*- coding utf-8 -*-
from django.db import models

from item import Item

class ItemLocation(models.Model):
    floor = models.PositiveSmallIntegerField(db_index=True)
    item = models.ForeignKey(Item)

    class Meta:
        db_table = 'item_location'
        unique_together = ('floor', 'item')
