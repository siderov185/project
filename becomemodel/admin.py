from django.contrib import admin
from becomemodel.models import BecomeModel

@admin.register(BecomeModel)
class BecomeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',]
