from django.urls import path
from article_module import views

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='articles_list'),
    path('cat/<str:category>', views.ArticlesListView.as_view(), name='articles_by_category_list'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='articles_detail'),
    path('add-article-comment', views.add_article_comment, name='add_article_comment'),
]