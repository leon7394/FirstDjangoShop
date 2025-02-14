from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .forms import ContactUsModelForm
from .models import ContactUs

class ContactUsView(View):

    def get(self, request):
        contact_form = ContactUsModelForm()
        return render(request, 'contact_module/contact_page.html', {'contact_form': contact_form})


    def post(self, request):
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home_page')

        return render(request, 'contact_module/contact_page.html', {'contact_form': contact_form})
