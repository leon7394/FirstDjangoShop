from urllib.parse import urlencode
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView
from article_module.models import Article
from utils.my_decorators import permission_checker_decorator


#*****************************************************************************************************************************

@permission_checker_decorator
def index(request):
    return render(request, 'admin_panel/home/index.html')

#*****************************************************************************************************************************

@method_decorator(permission_checker_decorator, name='dispatch')
class ArticlesListView(ListView):
    model = Article
    paginate_by = 20
    template_name = 'admin_panel/articles/articles_list.html'

#*****************************************************************************************************************************

@method_decorator(permission_checker_decorator, name='dispatch')
class ArticleEditView(UpdateView):
    model = Article
    template_name = 'admin_panel/articles/edit_article.html'
    success_url = reverse_lazy('admin_articles')
    fields = '__all__'


#*****************************************************************************************************************************
