from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from article_module.models import Article



# class ArticlesView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active=True)
#         return render(request, 'article_module/articles_page.html', {'articles': articles})

class ArticlesListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'
    context_object_name = 'articles'
