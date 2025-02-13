from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactUsForm
from .models import ContactUs


def contact_us_page(request):
    if request.method == "POST":
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)

            contact = ContactUs(
                full_name=contact_form.cleaned_data['full_name'],
                email=contact_form.cleaned_data['email'],
                title=contact_form.cleaned_data['title'],
                message=contact_form.cleaned_data['message'],
            )
            contact.save()

            return redirect('home_page')
    else:
        contact_form = ContactUsForm()

    return render(request, 'contact_module/contact_page.html', {
        'contact_form': contact_form
    })
