# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals, print_function

from six import text_type

from . import choices, models

from xyz_util.dateutils import get_next_date
from xyz_util.statutils import group_by
from django.contrib.contenttypes.models import ContentType


def sync_qcloud_vod_info(v):
    from xyz_qcloud import vod
    from xyz_qcloud.utils import access as A
    fid = v.context.get('fileId') or v.context.get('FileId')
    if not fid:
        return
    vc = v.context = A(vod.get_media_info(fid), 'MediaInfoSet.0')
    v.cover_url = A(vc, 'BasicInfo.CoverUrl')
    v.duration = A(vc, 'MetaData.Duration')
    v.size = A(vc, 'TranscodeInfo.TranscodeSet.0.Size')
    v.status = choices.STATUS_DONE
    v.save()


def noticeForgetExcerciseViewer(begin_date=None, end_date=None, uids=None):
    from xyz_exam.models import Paper
    from .models import Video
    from xyz_dailylog.models import Performance
    from xyz_message.helper import create_task
    from django.contrib.contenttypes.models import ContentType
    from xyz_util.datautils import list_dict
    from datetime import date, timedelta
    begin_date = begin_date or date.today() - timedelta(days=1)
    end_date = end_date or begin_date + timedelta(days=1)
    pct = ContentType.objects.get_for_model(Paper)
    vct = ContentType.objects.get_for_model(Video)
    vd = list_dict(Paper.objects.filter(owner_type=vct).values_list('owner_id', 'id'))
    if isinstance(uids, text_type):
        from xyz_auth.helper import find_user_ids_by_tag
        uids = list(find_user_ids_by_tag(uids))
        print(uids)
    for vid, pids in vd.items():
        lookup = dict(
            owner_type=vct,
            owner_id=vid,
            percent__gte=30,
            update_time__gte=begin_date,
            update_time__lt=end_date
        )
        if uids is not None:
            lookup['user_id__in'] = uids
        vqset = Performance.objects.filter(**lookup).values_list('user_id', flat=True)
        vuids = set(vqset)
        if (len(vuids) > 0):
            pqset = Performance.objects.filter(
                owner_type=pct,
                owner_id__in=pids
            ).values_list('user_id', flat=True)
            puids = set(pqset)
            fuids = vuids.difference(puids)
            if fuids:
                video = Video.objects.get(id=vid)
                tag = '用户.ID:%s' % ','.join([unicode(uid) for uid in fuids])
                unique_id = None if uids is not None else "video.has_exer:%d@%s" % (
                vid, begin_date.isoformat().replace('-', '')[2:8])
                print(unique_id, create_task(
                    tag,
                    '您观看的视频<%s>有配套习题, 请记得练习哦' % video.name,
                    link='/media/video/%d' % vid,
                    unique_id=unique_id
                ))


def update_object_new_video_count(owner):
    if isinstance(owner, tuple):
        owner_type, owner_id = owner
        owner = ContentType.objects.get_for_id(owner_type).get_object_for_this_type(pk=owner_id)
    else:
        owner_type = ContentType.objects.get_for_model(owner)
        owner_id = owner.id
    if hasattr(owner, 'data'):
        last_month = get_next_date(days=-30)
        new_count = models.Video.objects.filter(
            owner_type=owner_type,
            owner_id=owner_id,
            create_time__gt=last_month
        ).count()
        print(owner, new_count)
        owner.data['media_video_new_count'] = new_count
        owner.save()


def update_expire_objects_new_video_count(cond=None):
    if cond is None:
        date_begin = get_next_date(days=-31)
        date_end = get_next_date(days=-30)
        cond = dict(create_time__gt=date_begin, create_time__lt=date_end)
    qset = models.Video.objects.filter(**cond)
    for owner_type, owner_id, vcount in group_by(qset, ['owner_type', 'owner_id']):
        update_object_new_video_count((owner_type, owner_id))
