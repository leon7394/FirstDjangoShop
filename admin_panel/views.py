from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView
from article_module.models import Article

#*****************************************************************************************************************************

def index(request):
    return render(request, 'admin_panel/home/index.html')

#*****************************************************************************************************************************

class ArticlesListView(ListView):
    model = Article
    paginate_by = 20
    template_name = 'admin_panel/articles/articles_list.html'

#*****************************************************************************************************************************

class ArticleEditView(UpdateView):
    model = Article
    template_name = 'admin_panel/articles/edit_article.html'
    success_url = reverse_lazy('admin_articles')
    fields = '__all__'


#*****************************************************************************************************************************
