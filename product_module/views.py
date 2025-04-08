from django.shortcuts import redirect
from django.template.context_processors import request
from django.views.generic import ListView, DetailView, View
from .models import Product


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super().get_queryset()
        return base_query.filter(is_active=True, is_delete=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['products']
        for product in products:
            product.price_formatted = "{:,}".format(product.price).replace(",", "٬")

        return context



class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get('product_favorite')
        context['is_favorite'] = favorite_product_id == loaded_product.id
        product = context['product']
        context['price_formatted'] = "{:,}".format(product.price).replace(",", "٬")
        return context


class AddProductFavorite(View):
    def post(self, request):
        product_id = int(request.POST['product_id'])
        request.session['product_favorite'] = product_id
        product = Product.objects.get(pk=product_id)
        return redirect(product.get_absolute_url())



