from django.contrib import admin
from article_module.models import ArticleCategory, Article


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('selected_categories',)
    list_display = ['title', 'slug', 'is_active']
    list_editable = ['is_active']

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'parent', 'is_active']

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)