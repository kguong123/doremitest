# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20170530_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='modify_date',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='viewcount',
        ),
    ]
