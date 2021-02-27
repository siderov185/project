from django.contrib import admin
from contacts.models import Contacts, ContactMessage
# Register your models here.


class ContactsAdmin(admin.ModelAdmin):
    model = Contacts

    list_filter = (
        'title',
        'company',
        'address',
        'active',
    )

    list_display = (
        'title',
        'company',
        'address',
        'active',
    )


admin.site.register(Contacts, ContactsAdmin)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    model = ContactMessage
    readonly_fields = ['name', 'family_name', 'mail_address', 'subject', 'message']

    list_display = (
        'name',
        'family_name',
        'subject',
        'mail_address',
    )