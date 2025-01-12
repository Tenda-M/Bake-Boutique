from django.contrib import admin
from .models import ContactUsForm

@admin.register(ContactUsForm)
class ContactUsFormAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('name', 'email', 'read',)
