from django.urls import path
from admin_panel import views
from admin_panel.views import ArticlesListView

urlpatterns = [
    path('', views.index, name='admin_dashboard'),
    path('articles/', ArticlesListView.as_view(), name='admin_articles'),
    path('articles/edit/<pk>', views.ArticleEditView.as_view(), name='admin_edit_article'),
]