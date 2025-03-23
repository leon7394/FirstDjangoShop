from django.views.generic import CreateView
from .forms import ContactUsModelForm


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_page.html'
    form_class = ContactUsModelForm
    success_url = '/'

    # def get_success_url(self):
    #     return reverse('home_page')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

