# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-10-12 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_auto_20200809_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='outline',
            field=models.TextField(blank=True, default='', help_text='\u53ef\u5728\u6bcf\u4e00\u884c\u6700\u540e\u52a0\u4e0a\u65f6\u95f4\u70b9\uff0c \u683c\u5f0f\u6837\u4f8b: [03:12]', verbose_name='\u5927\u7eb2'),
        ),
    ]
