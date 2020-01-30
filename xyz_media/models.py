# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey

from django.contrib.auth.models import User
from xyz_util import modelutils


class Video(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "视频"

    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="media_videos",
                             on_delete=models.PROTECT)
    owner_type = models.ForeignKey(ContentType, verbose_name='属主类别', null=True, blank=True,
                                   on_delete=models.PROTECT)
    owner_id = models.PositiveIntegerField(verbose_name='属主编号', null=True, blank=True)
    owner = GenericForeignKey('owner_type', 'owner_id')
    name = models.CharField("名称", max_length=255)
    description = models.CharField("描述", max_length=255, null=True, blank=True, default='')
    url = models.URLField("网址")
    context = modelutils.JSONField("详情", blank=True, default={})
    is_active = models.BooleanField("有效", blank=False, default=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)

    def __unicode__(self):
        return self.name


class Image(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "图片"

    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="media_images",
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

