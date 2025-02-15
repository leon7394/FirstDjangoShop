from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView
from .forms import ContactUsModelForm
from .models import ContactUs


class ContactUsView(FormView):
    template_name = 'contact_module/contact_page.html'
    form_class = ContactUsModelForm
    # success_url = '/'

    def get_success_url(self):
        return reverse('home_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

