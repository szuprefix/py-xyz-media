# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2021-10-24 14:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '0007_auto_20210804_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.PositiveIntegerField(blank=True, db_index=True, null=True, verbose_name='\u5c5e\u4e3b\u7f16\u53f7')),
                ('name', models.CharField(max_length=255, verbose_name='\u540d\u79f0')),
                ('url', models.URLField(verbose_name='\u7f51\u5740')),
                ('duration', models.PositiveSmallIntegerField(blank=True, default=0, editable=False, help_text='\u5355\u4f4d: \u79d2.', verbose_name='\u65f6\u957f')),
                ('size', models.PositiveIntegerField(blank=True, default=0, editable=False, help_text='\u5355\u4f4d: \u6bd4\u7279Byte', verbose_name='\u5927\u5c0f')),
                ('is_active', models.BooleanField(default=False, verbose_name='\u6709\u6548')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('owner_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType', verbose_name='\u5f52\u7c7b')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='media_audios', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ('owner_type', 'owner_id', 'name'),
                'verbose_name': '\u97f3\u9891',
                'verbose_name_plural': '\u97f3\u9891',
            },
        ),
    ]
