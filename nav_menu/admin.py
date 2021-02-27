from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from nav_menu.models import NavMenu


class NavMenuAdmin(TranslationAdmin):
    model = NavMenu

    list_display = (
        'title',
        'link',
        'is_first_level',
        'order',
    )


admin.site.register(NavMenu, NavMenuAdmin)
