# -*- coding:utf-8 -*-
from __future__ import division, unicode_literals

from xyz_dailylog.mixins import ViewsMixin
from xyz_restful.mixins import UserApiMixin, BatchActionMixin
from rest_framework.response import Response
from xyz_util.statutils import do_rest_stat_action
from django_filters.rest_framework import DjangoFilterBackend
from . import models, serializers, stats, helper
from rest_framework import viewsets, decorators
from xyz_restful.decorators import register

@register()
class LecturerViewSet(viewsets.ModelViewSet):
    queryset = models.Lecturer.objects.all()
    serializer_class = serializers.LecturerSerializer
    search_fields = ('name',)
    filter_fields = {
        'id': ['in', 'exact'],
    }


    @decorators.action(['GET', 'POST'], detail=True)
    def avatar_signature(self, request, pk):
        from xyz_qcloud.cos import gen_signature
        return Response(gen_signature(allow_prefix='/media/lecturer/avatar/%s.*' % self.get_object().id))

@register()
class VideoViewSet(ViewsMixin, UserApiMixin, BatchActionMixin, viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
    search_fields = ('name',)
    filter_fields = {
        'id': ['in', 'exact'],
        'is_active': ['exact'],
        'owner_type': ['exact'],
        'owner_id': ['exact', 'in'],
        'lecturer': ['exact', 'in'],
    }
    ordering_fields = ('is_active', 'name', 'create_time', 'owner_type')

    @decorators.action(['POST'], detail=False)
    def batch_active(self, request):
        return self.do_batch_action('is_active', True)

    @decorators.action(['POST'], detail=False)
    def batch_update_media_info(self, request):
        return self.do_batch_action(helper.sync_qcloud_vod_info)

    @decorators.action(['GET', 'POST'], detail=False)
    def signature(self, request):
        from xyz_qcloud.vod import gen_signature
        return Response({'signature': gen_signature(extra_params="procedure=流畅")})

    @decorators.action(['get'], detail=False)
    def stat(self, request):
        return do_rest_stat_action(self, stats.stats_video)

    @decorators.action(['GET'], detail=False, filter_backends=[DjangoFilterBackend])
    def count(self, request):
        c = self.filter_queryset(self.get_queryset()).count()
        return Response({'count': c})


@register()
class ImageViewSet(UserApiMixin, BatchActionMixin, viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    filter_fields = {
        'id': ['in', 'exact'],
        'is_active': ['exact'],
        'owner_type': ['exact'],
        'owner_id': ['exact', 'in'],
    }
    ordering_fields = ('is_active', 'create_time', 'owner_type')

    @decorators.action(['POST'], detail=False)
    def batch_active(self, request):
        return self.do_batch_action('is_active', True)

    @decorators.action(['GET', 'POST'], detail=False)
    def signature(self, request):
        d = request.query_params
        owner_type = d.get('owner_type')
        owner_id = d.get('owner_id')
        from xyz_qcloud.cos import gen_signature
        return Response(gen_signature(allow_prefix='%s/%s/images/*' % (owner_type.replace('.', '/'), owner_id)))


    @decorators.action(['GET', 'POST'], detail=False)
    def user_signature(self, request):
        d = request.query_params
        uid = request.user.id
        owner_type = d.get('owner_type')
        owner_id = d.get('owner_id')
        from xyz_qcloud.cos import gen_signature
        return Response(gen_signature(allow_prefix='%s/%s/images/u%s/*' % (owner_type.replace('.', '/'), owner_id, uid)))


