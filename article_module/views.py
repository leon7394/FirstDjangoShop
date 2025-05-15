from django.shortcuts import render
from django.views.generic import ListView, DetailView
from article_module.models import Article, ArticleCategory


class ArticlesListView(ListView):
    model = Article
    paginate_by = 4
    template_name = 'article_module/articles_page.html'
    context_object_name = 'articles'

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

def article_categories_component(request):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)
    return render(request, 'article_module/components/article_categories_component.html', {'main_categories': article_main_categories})
