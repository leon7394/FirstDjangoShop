from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from user_panel_module.forms import EditProfileModelForm


class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login_page'))
        return super().dispatch(request, *args, **kwargs)

class EditUserProfilePage(View):
    def get(self, request):
        edit_form = EditProfileModelForm()
        context = {
            'form' : edit_form
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request):
        return render(request, 'user_panel_module/edit_profile_page.html', {})


def user_panel_menu_component(request):
    return render(request, "user_panel_module/components/user_panel_menu_component.html")