from django.contrib import admin
from . import models

class ContactFunction(admin.ModelAdmin):
    list_display = ['full_name', 'created_date']
    fields = ('full_name', 'email', 'title', 'message', 'created_date', 'response', 'is_read_by_admin')
    readonly_fields = ('created_date',)

admin.site.register(models.ContactUs, ContactFunction)