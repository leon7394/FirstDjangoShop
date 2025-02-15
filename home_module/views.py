from django.shortcuts import render
from django.utils.translation.template import context_re
from django.views import View
from django.views.generic.base import TemplateView



class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'This is My first Django Shop! '
        return context


def site_header_component(request):
    content = {
        'link' : 'پنل ادمین'
    }
    return render(request, 'shared/site_header_component.html', content)

def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')