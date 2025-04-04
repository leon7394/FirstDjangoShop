from django.views.generic import CreateView, ListView
from .forms import ContactUsModelForm
from .models import UserProfile


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_page.html'
    form_class = ContactUsModelForm
    success_url = '/'
    # def get_success_url(self):
    #     return reverse('home_page')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)



class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/create-profile/'


class ProfilesView(ListView):
    template_name = 'contact_module/profiles_list_page.html'
    model = UserProfile
    context_object_name = 'profiles'