# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('requester', models.CharField(max_length=64)),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('floor', models.PositiveIntegerField(default=11, db_index=True)),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('item', models.ForeignKey(to='kitchen_app.Item')),
            ],
            options={
                'db_table': 'request',
            },
        ),
    ]
