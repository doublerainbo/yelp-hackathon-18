# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen_app', '0005_auto_20151113_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(unique=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='request',
            name='item',
            field=models.ForeignKey(to='kitchen_app.ItemLocation'),
        ),
    ]
