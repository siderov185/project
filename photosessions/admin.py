from django.contrib import admin
from photosessions.models import PhotoSessions


@admin.register(PhotoSessions)
class PhotoSessionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photos',]
