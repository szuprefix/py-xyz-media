# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals
from . import models
from django_szuprefix.utils import statutils


def stats_video(qset=None, measures=None, period=None):
    qset = qset if qset is not None else models.Video.objects.all()
    qset = statutils.using_stats_db(qset)
    dstat = statutils.DateStat(qset, 'create_time')
    funcs = {
        'today': lambda: dstat.stat("今天", count_field="id", only_first=True),
        'yesterday': lambda: dstat.stat("昨天", count_field="id", only_first=True),
        'all': lambda: qset.values("id").distinct().count(),
        'count': lambda: dstat.get_period_query_set(period).count(),
        'owner_type': lambda: statutils.count_by(
            dstat.get_period_query_set(period),
            'owner_type__model',
            count_field='owner_type',
            distinct=True, sort="-"),
        'owner_id': lambda: statutils.count_by(
            dstat.get_period_query_set(period),
            'owner_type,owner_id',
            count_field='id',
            distinct=True, sort="-"),
    }
    return dict([(m, funcs[m]()) for m in measures])


def stats_fault(qset=None, measures=None, period=None):
    qset = qset if qset is not None else models.Fault.objects.all()
    qset = statutils.using_stats_db(qset)
    dstat = statutils.DateStat(qset, 'update_time')
    funcs = {
        'today': lambda: dstat.stat("今天", count_field="user_id", distinct=True, only_first=True),
        'count': lambda: dstat.get_period_query_set(period).count(),
        'all': lambda: qset.values("user_id").distinct().count(),
    }
    return dict([(m, funcs[m]()) for m in measures])

