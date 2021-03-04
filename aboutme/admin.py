from django.contrib import admin
from aboutme.models import AboutMe

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo',]
