from django.contrib import admin
from article_module.models import ArticleCategory, Article, ArticleComment

#****************************************************************************************************************************

@admin.register(Article )
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('selected_categories',)
    list_display = ['title', 'slug', 'is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        return super(ArticleAdmin, self).save_model(request, obj, form, change)


#****************************************************************************************************************************

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'parent', 'is_active']

#****************************************************************************************************************************

admin.site.register(ArticleComment)

#****************************************************************************************************************************

