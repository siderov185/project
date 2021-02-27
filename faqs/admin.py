from django.contrib import admin
from modeltranslation.translator import register, TranslationOptions
from modeltranslation.admin import TranslationAdmin
from faqs.models import Faqs

# @admin.register(Faqs)


class FaqsAdmin(TranslationAdmin):
    # model = Faqs
    fields = ('question', 'answer')

    # list_filter = (
    #     'question',
    #     'answer',
    #     # 'sequence',
    #     # 'active',
    # )

    # list_display = (
    #     'question',
    #     'answer',
    #     # 'sequence',
    #     # 'active',
    # )


admin.site.register(Faqs)