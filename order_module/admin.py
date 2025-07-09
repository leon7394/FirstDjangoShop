from django.contrib import admin
from order_module import models

admin.site.register(models.Order)
admin.site.register(models.OrderDetail)