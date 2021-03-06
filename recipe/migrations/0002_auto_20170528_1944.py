# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import recipe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='foodname',
            field=models.CharField(max_length=25, verbose_name='\uc74c\uc2dd \uc774\ub984'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=50, verbose_name='\ub808\uc2dc\ud53c \uc124\uba85'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='titleimage',
            field=recipe.fields.ThumbnailImageField(upload_to='Recipe/titleiamge/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='recipeinfo',
            name='image',
            field=recipe.fields.ThumbnailImageField(upload_to='Recipe/content/%y/%m/%d'),
        ),
    ]
