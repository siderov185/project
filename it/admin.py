from django.contrib import admin
from it.models import It

@admin.register(It)
class ItAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
