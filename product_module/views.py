from django.db.models import Count
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View
from site_module.models import SiteBanner
from utils.convertors import group_list
from utils.http_service import get_client_ip
from .models import Product, ProductCategory, ProductBrand, ProductVisit, ProductGallery


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6


    def get_queryset(self):
        query = super().get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        my_request = self.request
        start_price = my_request.GET.get('start_price')
        end_price = my_request.GET.get('end_price')

        if start_price:
            query = query.filter(price__gte=start_price)

        if end_price:
            query = query.filter(price__lte=end_price)

        if brand_name:
            query = query.filter(brand__url_title__iexact=brand_name, is_active=True, is_delete=False)

        if category_name:
            query = query.filter(category__url_title__iexact=category_name, is_active=True, is_delete=False)

        return query


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = Product.objects.all()
        product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 100000000
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['banners'] = SiteBanner.objects.filter(is_active=True, position__iexact=SiteBanner.SiteBannerPositions.product_list)
        products = context['products']

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
        context['banners'] = SiteBanner.objects.filter(is_active=True, position__iexact=SiteBanner.SiteBannerPositions.product_detail)
        context['product_galleries_group'] = group_list(list(ProductGallery.objects.filter(product_id=loaded_product.id).all()),3)
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_product.id).exists()
        if not has_been_visited:
            new_visit = ProductVisit(product=loaded_product, ip=user_ip, user_id=user_id)
            new_visit.save()

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



def product_brand_component(request):
    product_brands = ProductBrand.objects.filter(is_active=True).annotate(products_count=Count('product'))
    context = {
        'brands' : product_brands,
    }
    return render(request, 'product_module/components/product_brand_component.html', context)