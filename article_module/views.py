from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from article_module.models import Article, ArticleCategory, ArticleComment


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

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(article_id = article.id, parent=None).order_by('-create_date').prefetch_related('articlecomment_set')
        context['comments_count'] = ArticleComment.objects.filter(article_id=article.id).count()
        return context

def article_categories_component(request):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)
    return render(request, 'article_module/components/article_categories_component.html', {'main_categories': article_main_categories})


def add_article_comment(request):
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        parent_id = request.GET.get('parent_id')
        article_comment = request.GET.get('article_comment')
        new_comment = ArticleComment(article_id = article_id, text = article_comment, user_id = request.user.id, parent_id=parent_id)
        new_comment.save()
        context = {
            'comments': ArticleComment.objects.filter(article_id = article_id, parent=None).order_by('-create_date').prefetch_related('articlecomment_set'),
            'comments_count' : ArticleComment.objects.filter(article_id=article_id).count()
        }
        return render(request, 'article_module/includes/article_comments_partial.html', context)

    return HttpResponse('hello')