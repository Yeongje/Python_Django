# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20171005_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='Major',
            field=models.CharField(max_length=50),
        ),
    ]
