from django.views.generic import CreateView, ListView
from site_module.models import SiteSetting
from .forms import ContactUsModelForm
from .models import UserProfile


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_page.html'
    form_class = ContactUsModelForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context



class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/create-profile/'


class ProfilesView(ListView):
    template_name = 'contact_module/profiles_list_page.html'
    model = UserProfile
    context_object_name = 'profiles'