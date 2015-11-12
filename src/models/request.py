from django.db import models
from item import Item

class Request(models.Model):
    requester = models.CharField(max_length=64)
    request_time = models.DateTimeField(auto_now_add=True)
    floor = models.PositiveIntegerField(default=11, db_index=True)
    item = models.ForeignKey(Item)
    status = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'request'
