# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('honeytip', '0004_auto_20170611_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='HhoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(default='', max_length=100, verbose_name='slug')),
                ('user', models.CharField(default='', max_length=100, verbose_name='user')),
                ('comments', models.TextField(null=True, verbose_name='comments')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create Date')),
                ('honeycomment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='honeytip.HoneyTip')),
            ],
        ),
    ]