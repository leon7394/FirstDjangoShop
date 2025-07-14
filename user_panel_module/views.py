from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from account_module.models import User
from order_module.models import Order, OrderDetail
from user_panel_module.forms import EditProfileModelForm, ChangePasswordForm
from django.contrib.auth import logout

@method_decorator(login_required, name='dispatch')
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = User.objects.filter(id=self.request.user.id).first()
        context['current_user'] = current_user
        return context




@method_decorator(login_required, name='dispatch')
class EditUserProfilePage(View):

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




@method_decorator(login_required, name='dispatch')
class ChangePasswordPage(View):

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




@login_required
def user_panel_menu_component(request):
    return render(request, "user_panel_module/components/user_panel_menu_component.html")




@login_required
def user_basket(request):
    current_order, created = Order.objects.prefetch_related('order_details').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order' : current_order,
        'sum' : total_amount,
    }
    return render(request, 'user_panel_module/user_basket.html', context)




@login_required
def remove_order_detail(request):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({'status':'not_found_detail_id'})

    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id, is_paid=False, order__user_id=request.user.id).delete()
    if deleted_count == 0 :
        return JsonResponse({
            'status':'detail_not_found'
        })

    current_order, created = Order.objects.prefetch_related('order_details').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order' : current_order,
        'sum' : total_amount,
    }
    data = render_to_string('user_panel_module/user_basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'body' : data
    })





@login_required
def change_order_detail_count(request):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_or_state'
        })

    order_detail = OrderDetail.objects.filter(id = detail_id, order__user_id=request.user.id, order__is_paid=False).first()
    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
    elif state == 'decrease':
        if order_detail.count == 1 :
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid'
        })

    current_order, created = Order.objects.prefetch_related('order_details').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order' : current_order,
        'sum' : total_amount,
    }

    data = render_to_string('user_panel_module/user_basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'body' : data
    })