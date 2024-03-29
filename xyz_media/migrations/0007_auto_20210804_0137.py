# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2021-08-04 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_auto_20201020_0202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('-create_time',), 'verbose_name': '\u56fe\u7247', 'verbose_name_plural': '\u56fe\u7247'},
        ),
        migrations.AlterField(
            model_name='attachment',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='\u6709\u6548'),
        ),
        migrations.AlterField(
            model_name='image',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='\u6709\u6548'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='\u63cf\u8ff0'),
        ),
    ]
