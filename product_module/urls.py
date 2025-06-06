from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product-categories-list'),
    re_path(r'^(?P<slug>[-\w\u0600-\u06FF]+)/$', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-favorite', views.AddProductFavorite.as_view() , name='product-favorite'),
]