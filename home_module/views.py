from django.db.models.aggregates import Count, Sum
from django.shortcuts import render
from django.views.generic.base import TemplateView

from product_module.models import Product, ProductCategory
from site_module.models import SiteSetting, FooterLinkBox, Slider
from utils.convertors import group_list


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'فروشگاه لئون | صفحه اصلی'
        context['sliders'] = Slider.objects.filter(is_active=True)
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        most_visit_product = Product.objects.filter(is_active=True, is_delete=False).annotate(
            visit_count=Count('product_visits')).order_by('-visit_count')[:12]

        context['latest_products'] = group_list(latest_products)
        context['most_visit_products'] = group_list(most_visit_product)
        categories = list(ProductCategory.objects.annotate(products_count=Count('product_categories')).filter(is_active=True, is_delete=False, products_count__gt=0)[:6])
        categories_products = []
        for category in categories:
            categories_products.append(
                {
                    'id' : category.id,
                    'title' : category.title,
                    'products' : list(category.product_categories.all()[:4])
                }
            )
        context['categories_products'] = categories_products

        most_bought_products = Product.objects.filter(orderdetail__order__is_paid=True).annotate(order_count=Sum('orderdetail__count')).order_by('-order_count')[:12]
        context['most_bought_products'] = group_list(most_bought_products)

        return context


def site_header_component(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting,
        'link' : 'پنل ادمین',
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes,
    }
    return render(request, 'shared/site_footer_component.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['site_setting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        return context