from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)  # برای نمایش دسته‌بندی به‌صورت دو لیست کنار هم

    list_filter = ['category', 'is_active']
    list_display_links = ('id', 'title')
    list_display = ['id', 'title', 'price', 'is_active', 'is_delete']
    # list_editable = ['title', 'price', 'is_active', 'is_delete']

#***********************************************************************************************************************

@admin.register(models.ProductComment)
class ProductComments(admin.ModelAdmin):
    list_display = ['user' , 'create_date' ,'text']

#***********************************************************************************************************************

admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductVisit)
admin.site.register(models.ProductGallery)