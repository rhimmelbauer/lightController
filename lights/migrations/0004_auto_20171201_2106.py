# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0003_auto_20171201_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bulb',
            old_name='zone_id',
            new_name='zone',
        ),
    ]