# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen_app', '0002_remove_request_floor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('floor', models.PositiveSmallIntegerField(db_index=True)),
                ('item', models.ForeignKey(to='kitchen_app.Item')),
            ],
            options={
                'db_table': 'item_location',
            },
        ),
        migrations.AlterUniqueTogether(
            name='itemlocation',
            unique_together=set([('floor', 'item')]),
        ),
    ]
