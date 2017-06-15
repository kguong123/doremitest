# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20170603_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodinfo',
            name='ingredient',
            field=models.CharField(blank=True, max_length=200, verbose_name='\uc7ac\ub8cc\uc815\ubcf4'),
        ),
        migrations.AlterField(
            model_name='foodinfo',
            name='quantity',
            field=models.CharField(blank=True, help_text='\uc7ac\ub8cc\ub7c9: \ud3ec\uae30, \uac1c, \uacf5\uae30', max_length=200, verbose_name='\uc7ac\ub8cc\ub7c9: \ud3ec\uae30, \uac1c, \uacf5\uae30'),
        ),
    ]