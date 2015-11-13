# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen_app', '0003_auto_20151113_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='employee_location',
            field=models.CharField(default=b'Unspecified', max_length=200),
        ),
    ]
