# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20160518_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='online',
        ),
        migrations.DeleteModel(
            name='Online',
        ),
    ]
