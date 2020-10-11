# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from . import choices
from django.contrib.auth.models import User
from xyz_util import modelutils

class Lecturer(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "讲师"
        ordering = ('name',)

    avatar = models.URLField("头像", null=True, blank=True)
    name = models.CharField("名称", max_length=255)
    description = models.CharField("描述", max_length=255, null=True, blank=True, default='')
    create_time = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)

    def __unicode__(self):
        return self.name

class Video(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "视频"
        ordering = ('owner_type', 'owner_id', 'name')

    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="media_videos",
                             on_delete=models.PROTECT)
    owner_type = models.ForeignKey('contenttypes.ContentType', verbose_name='归类', null=True, blank=True,
                                   on_delete=models.PROTECT)
    owner_id = models.PositiveIntegerField(verbose_name='属主编号', null=True, blank=True, db_index=True)
    owner = GenericForeignKey('owner_type', 'owner_id')
    name = models.CharField("名称", max_length=255)
    description = models.CharField("描述", max_length=255, null=True, blank=True, default='')
    url = models.URLField("网址")
    cover_url = models.URLField('封面', blank=True, null=True)
    duration = models.PositiveSmallIntegerField('时长', blank=True, default=0, help_text='单位: 秒.', editable=False)
    size = models.PositiveIntegerField('大小', blank=True, default=0, help_text='单位: 比特Byte', editable=False)
    context = modelutils.JSONField("详情", blank=True, default={})
    outline = models.TextField("大纲", blank=True, default='', help_text='可在每一行最后加上时间点， 格式样例: [03:12]')
    status = models.PositiveSmallIntegerField("状态", choices=choices.STATUS, blank=True, default=choices.STATUS_PROCESS)
    is_active = models.BooleanField("有效", blank=False, default=False)
    lecturer = models.ForeignKey(Lecturer, verbose_name=Lecturer._meta.verbose_name, blank=True, null=True, related_name="videos", on_delete=models.PROTECT)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)

    def __unicode__(self):
        return self.name


class Image(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "图片"

    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="media_images",
                             on_delete=models.PROTECT)
    owner_type = models.ForeignKey(ContentType, verbose_name='属主类别', null=True, blank=True,
                                   on_delete=models.PROTECT, related_name="media_images")
    owner_id = models.PositiveIntegerField(verbose_name='属主编号', null=True, blank=True, db_index=True)
    owner = GenericForeignKey('owner_type', 'owner_id')
    name = models.CharField("名称", max_length=255)
    # description = models.CharField("描述", max_length=255, null=True, blank=True, default='')
    url = models.URLField("网址")
    is_active = models.BooleanField("有效", blank=False, default=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)

    def __unicode__(self):
        return self.name


class Attachment(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "附件"

    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="media_attachments",
                             on_delete=models.PROTECT)
    owner_type = models.ForeignKey(ContentType, verbose_name='属主类别', null=True, blank=True,
                                   on_delete=models.PROTECT)
    owner_id = models.PositiveIntegerField(verbose_name='属主编号', null=True, blank=True)
    owner = GenericForeignKey('owner_type', 'owner_id')
    name = models.CharField("名称", max_length=255)
    description = models.CharField("描述", max_length=255, null=True, blank=True, default='')
    url = models.URLField("网址")
    is_active = models.BooleanField("有效", blank=False, default=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)

    def __unicode__(self):
        return self.name

