# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-08-09 00:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_remove_image_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('owner_type', 'owner_id', 'name'), 'verbose_name': '\u89c6\u9891', 'verbose_name_plural': '\u89c6\u9891'},
        ),
        migrations.AlterField(
            model_name='image',
            name='owner_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True, verbose_name='\u5c5e\u4e3b\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='image',
            name='owner_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='media_images', to='contenttypes.ContentType', verbose_name='\u5c5e\u4e3b\u7c7b\u522b'),
        ),
    ]
