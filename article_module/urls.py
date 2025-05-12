from django.urls import path
from article_module import views

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='articles_list'),
]