# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals,print_function
from . import models, choices, helper
from .helper import noticeForgetExcerciseViewer, update_expire_objects_new_video_count

def sync_video_info():
    print('sync_video_info')
    for v in models.Video.objects.filter(status=choices.STATUS_PROCESS):
        print(v)
        helper.sync_qcloud_vod_info(v)
