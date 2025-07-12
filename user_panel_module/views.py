from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from account_module.models import User
from order_module.models import Order
from user_panel_module.forms import EditProfileModelForm, ChangePasswordForm
from django.contrib.auth import logout

class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login_page'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = User.objects.filter(id=self.request.user.id).first()
        context['current_user'] = current_user
        return context



class EditUserProfilePage(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login_page'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)
        context = {
            'form' : edit_form,
            'current_user' : current_user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)

        context = {
            'form' : edit_form,
            'current_user' : current_user,
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)



class ChangePasswordPage(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login_page'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        context = {
            'form' : ChangePasswordForm(),
            'current_user': current_user,
        }
        return render(request, 'user_panel_module/change_password_page.html', context)

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        current_user = User.objects.filter(id=request.user.id).first()
        if form.is_valid():
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('current_password', 'کلمه عبور وارد شده اشتباه است')

        context = {
            'form' : form,
            'current_user' : current_user,
        }
        return render(request, 'user_panel_module/change_password_page.html', context)


def user_panel_menu_component(request):
    return render(request, "user_panel_module/components/user_panel_menu_component.html")


def user_basket(request):
    current_order, created = Order.objects.prefetch_related('order_details').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = 0
    for order_detail in current_order.order_details.all():
        total_amount += order_detail.count * order_detail.product.price

    context = {
        'order' : current_order,
        'sum' : total_amount,
    }
    return render(request, 'user_panel_module/user_basket.html', context)