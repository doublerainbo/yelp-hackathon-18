# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen_app', '0004_request_employee_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.AlterField(
            model_name='request',
            name='requester',
            field=models.ForeignKey(to='kitchen_app.Employee'),
        ),
    ]
