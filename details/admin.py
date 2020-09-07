from django.contrib import admin
from .models import ContactUsMessage

@admin.register(ContactUsMessage)
class ContactUsMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','created_date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'created_date'

