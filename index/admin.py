from django.contrib import admin
from index.models import Index

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',]
