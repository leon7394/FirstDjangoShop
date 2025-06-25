from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)  # برای نمایش دسته‌بندی به‌صورت دو لیست کنار هم

    list_filter = ['category', 'is_active']
    list_display_links = ('id', 'title')
    list_display = ['id', 'title', 'price', 'is_active', 'is_delete']
    # list_editable = ['title', 'price', 'is_active', 'is_delete']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductVisit)