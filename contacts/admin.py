from django.contrib import admin
from contacts.models import Contacts

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'description', 'text']


