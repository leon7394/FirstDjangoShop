from django.urls import path, re_path
from . import views

urlpatterns = [
    path('add-comment/', views.ProductCommentCreateView.as_view(), name='add_product_comment'),
    path('', views.ProductListView.as_view(), name='product-list'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product-categories-list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product-list-by-brands'),
    path('product-favorite', views.AddProductFavorite.as_view() , name='product-favorite'),
    re_path(r'^(?P<slug>[-\w\u0600-\u06FF]+)/$', views.ProductDetailView.as_view(), name='product-detail'),
]