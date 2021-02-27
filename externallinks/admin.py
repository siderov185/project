from django.contrib import admin
from modeltranslation.translator import register, TranslationOptions
from modeltranslation.admin import TranslationAdmin
from externallinks.models import ExternalLinks


class ExternalLinksAdmin(TranslationAdmin):
    # model = ExternalLinks
    fields = ('title', 'short_description')
    # list_filter = (
    #     'title',
    #     'active',
    #     'short_description',
    # )
    #
    # list_display = (
    #     'title',
    #     'active',
    #     'short_description',
    # )


admin.site.register(ExternalLinks, ExternalLinksAdmin)
