# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0005_auto_20171203_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulb',
            name='ipAddr',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
