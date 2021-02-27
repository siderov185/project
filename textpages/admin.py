from django.contrib import admin
from textpages.models import TextPages


class TextPagesAdmin(admin.ModelAdmin):
    model = TextPages

    list_filter = (
        'title',
        'meta_description',
    )

    list_display = (
        'title',
        'meta_description',
        'active',
        'description'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(TextPages, TextPagesAdmin)
