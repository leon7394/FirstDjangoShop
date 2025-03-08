from django.contrib import admin
from . import models


class ContactFunction(admin.ModelAdmin):
    list_display = ['full_name', 'get_shamsi_date']
    fields = ('full_name', 'email', 'title', 'message', 'created_date', 'get_shamsi_date', 'response', 'is_read_by_admin')
    readonly_fields = ('created_date','get_shamsi_date')

    def get_shamsi_date(self, obj):
        return obj.get_shamsi_date()

    get_shamsi_date.short_description = "تاریخ شمسی"

admin.site.register(models.ContactUs, ContactFunction)
