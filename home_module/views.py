from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, 'home_module/index_page.html')

def contact_page(request):
    return render(request, 'home_module/../contact_module/templates/contact_module/contact_page.html')

def site_header_component(request):
    content = {
        'link' : 'آموزش جنگو'
    }
    return render(request, 'shared/site_header_component.html', content)

def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')