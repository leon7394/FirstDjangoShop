from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Product


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super().get_queryset()
        return base_query.filter(is_active=True, is_delete=False)



class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

