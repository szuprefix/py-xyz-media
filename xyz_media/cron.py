# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals
from . import models, choices, helper


def sync_video_info():
    print 'sync_video_info'
    for v in models.Video.objects.filter(status=choices.STATUS_PROCESS):
        print v
        helper.sync_qcloud_vod_info(v)


def noticeForgetExcerciseViewer():
    helper.noticeForgetExcerciseViewer()
