from django.contrib import admin

from . import models


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('create_time', 'name', 'description', 'is_active', 'owner_type')
    raw_id_fields = ('user',)
    search_fields = ("name", "description")


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('create_time', 'name', 'is_active', 'owner_type')
    raw_id_fields = ('user',)
    search_fields = ("name", )
