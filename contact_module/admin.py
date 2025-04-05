from django.contrib import admin
from . import models


class ContactFunction(admin.ModelAdmin):

    def get_shamsi_date(self, obj):
        return obj.get_shamsi_date()

    get_shamsi_date.short_description = "تاریخ شمسی"

    list_display = ['title', 'full_name', 'get_shamsi_date']
    fields = ('full_name', 'email', 'title', 'message', 'created_date', 'get_shamsi_date', 'response', 'is_read_by_admin')
    readonly_fields = ('created_date','get_shamsi_date')



admin.site.register(models.ContactUs, ContactFunction)
admin.site.register(models.UserProfile)
