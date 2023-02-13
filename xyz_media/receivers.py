# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from django.dispatch import receiver
from django.conf import settings

from xyz_saas.signals import to_get_party_settings
from xyz_util.datautils import access
from django.db.models.signals import post_save
from . import models
import logging

log = logging.getLogger('django')

@receiver(to_get_party_settings)
def get_media_settings(sender, **kwargs):
    d = settings.QCLOUD
    return {
        'media': {
            'qcloud': {
                'cos': {
                    'bucket': access(d, 'COS.BUCKET')
                },
                'vod': {
                    'appid': access(d, 'VOD.SUB_APP_ID')
                }
            }
        }
    }


@receiver(post_save, sender=models.Video)
def save_owner_new_video_count(sender, **kwargs):
    video = kwargs.get('instance')
    try:
        from .helper import update_object_new_video_count
        update_object_new_video_count(video.owner)
    except:
        import traceback
        log.error('save_owner_new_video_count error: %s', traceback.format_exc())
