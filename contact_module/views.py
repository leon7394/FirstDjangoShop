from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from .forms import ContactUsModelForm, ProfileForm
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



class CreateProfileView(View):
    @staticmethod
    def get(request):
        form = ProfileForm()
        return render(request, 'contact_module/create_profile_page.html', {'form': form})

    @staticmethod
    def post(request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return redirect('/create-profile')
        else:
            return render(request, 'contact_module/create_profile_page.html', {'form': submitted_form})
