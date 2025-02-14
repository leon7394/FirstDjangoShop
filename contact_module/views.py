from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsModelForm
from .models import ContactUs

def contact_us_page(request):
    if request.method == "POST":
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home_page')
    else:
        contact_form = ContactUsModelForm()

    return render(request, 'contact_module/contact_page.html', {
        'contact_form': contact_form
    })
