from django.shortcuts import render
from django.views.generic.base import TemplateView
from site_module.models import SiteSetting, FooterLinkBox


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hi, This is My first Django Shop! '
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