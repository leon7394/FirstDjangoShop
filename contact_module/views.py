from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactUsForm

def contact_us_page(request):
    contact_form = ContactUsForm(request.POST or None)

    if request.method == "POST":
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            return redirect('home_page')

    return render(request, 'contact_module/contact_page.html', {
        'contact_form': contact_form
    })
