# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-10-20 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_video_outline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(max_length=255, verbose_name='\u7f51\u5740'),
        ),
    ]
