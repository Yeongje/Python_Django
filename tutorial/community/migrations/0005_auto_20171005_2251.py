# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_auto_20171005_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='area',
        ),
        migrations.AddField(
            model_name='poll',
            name='party_number',
            field=models.IntegerField(default=1),
        ),
    ]
