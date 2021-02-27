from django.contrib import admin
from company.models import Company, CompanyFile, Politics, PoliticsFile
# Register your models here.


class CompanyFileInLineAdmin(admin.TabularInline):
    model = CompanyFile


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    inlines = [
        CompanyFileInLineAdmin,
    ]

    list_filter = (
        'title',
        'slug',
        'active',
    )

    list_display = (
        'title',
        'slug',
        'active',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }


class PoliticFileInLineAdmin(admin.TabularInline):
    model = PoliticsFile


class PoliticAdmin(admin.ModelAdmin):
    model = Politics
    inlines = [
        PoliticFileInLineAdmin,
    ]

    list_filter = (
        'title',
        'slug',
        'meta_key_words',
        'active',
    )

    list_display = (
        'title',
        'slug',
        'meta_key_words',
        'active',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Company, CompanyAdmin)
admin.site.register(Politics, PoliticAdmin)