from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View
from .models import Product, ProductCategory


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 3

    def get_queryset(self):
        query = super().get_queryset()
        category_name = self.kwargs.get('cat')
        if category_name:
            query = query.filter(category__url_title__iexact=category_name, is_active=True, is_delete=False)
        return query


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['products']
        for product in products:
            product.price_formatted = "{:,}".format(product.price)
        return context



class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get('favorite_product_id')
        context['is_favorite'] = favorite_product_id == loaded_product.id
        product = context['product']
        context['price_formatted'] = "{:,}".format(product.price)
        return context



class AddProductFavorite(View):
    def post(self, request):
        product_id = int(request.POST['product_id'])
        request.session['product_favorite'] = product_id
        product = Product.objects.get(pk=product_id)
        return redirect(product.get_absolute_url())



def product_categories_component(request):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories,
    }
    return render(request, 'product_module/components/product_categories_component.html', context)
