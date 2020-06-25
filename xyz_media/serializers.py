# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from xyz_restful.mixins import IDAndStrFieldSerializerMixin
from rest_framework import serializers
from . import models


class LecturerSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Lecturer
        fields = '__all__'
        read_only_fields = ('create_time',)



class VideoSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    lecturer_name = serializers.CharField(source="lecturer.name", read_only=True)
    class Meta:
        model = models.Video
        fields = '__all__'
        read_only_fields = ('user', 'create_time')


class ImageSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'
        read_only_fields = ('user', 'create_time')



