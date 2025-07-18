from django.contrib.auth import login,logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from utils.email_service import send_email
from .models import User
from account_module.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm

#*****************************************************************************************************************************

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'account_module/register.html', {'register_form': register_form})


    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده قبلا در سایت ثبت نام شده است')
                return render(request, 'account_module/register.html', {'register_form': register_form})
            else:
                new_user = User(
                    email = user_email,
                    email_active_code = get_random_string(72),
                    username = user_email,
                    is_active = False,
                )
                new_user.set_password(user_password)
                new_user.save()
                send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'email/activate_account.html')
                return redirect(reverse('login_page'))

        else:
            return render(request, 'account_module/register.html', {'register_form': register_form})

#*****************************************************************************************************************************

class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        return render(request, 'account_module/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).first()
            if user:
                if user.is_active:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        next_url = request.POST.get('next') or reverse('user_panel_dashboard')
                        return redirect(next_url)
                    else:
                        login_form.add_error('password', 'آدرس ایمیل یا رمز عبور وارد شده اشتباه است')
                else:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
            else:
                login_form.add_error('email', 'آدرس ایمیل یا رمز عبور وارد شده اشتباه است')


        return render(request, 'account_module/login.html', {'login_form': login_form})

#*****************************************************************************************************************************

class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user = User.objects.filter(email_active_code__iexact = email_active_code ).first()
        if user:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login_page'))
            else:
                return redirect(reverse('login_page'))
        else:
            raise Http404("کاربری با این کد فعال‌سازی پیدا نشد")

#*****************************************************************************************************************************

class ForgetPasswordView(View):
    def get(self, request):
        forget_pass_form = ForgotPasswordForm()
        return render(request, 'account_module/forget_password.html', {'forget_pass_form' : forget_pass_form})

    def post(self, request):
        forget_pass_form = ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact = user_email).first()
            if user:
                send_email('تغییر رمز عبور حساب کاربری', user.email, {'user': user}, 'email/forgot_password.html')
                return redirect(reverse('home_page'))
            else:
                forget_pass_form.add_error('email', 'کاربری با این ایمیل یافت نشد')

        return render(request, 'account_module/forget_password.html', {'forget_pass_form' : forget_pass_form})

#*****************************************************************************************************************************

class ResetPasswordView(View):
    def get(self, request, active_code):
        user = User.objects.filter(email_active_code__iexact = active_code).first()
        if user :
            reset_pass_form =  ResetPasswordForm()
            return render(request, 'account_module/reset_password.html', {
                'reset_pass_form': reset_pass_form,
                'user' : user
            })
        else:
            return redirect(reverse('login_page'))


    def post(self, request, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user = User.objects.filter(email_active_code__iexact = active_code).first()

        if reset_pass_form.is_valid():
            if user:
                user_new_pass = reset_pass_form.cleaned_data.get('password')
                user.set_password(user_new_pass)
                user.email_active_code = get_random_string(72)
                user.is_active = True
                user.save()
                return redirect(reverse('login_page'))
            else:
                return redirect(reverse('login_page'))
        else:
            return render(request, 'account_module/reset_password.html', {
                'reset_pass_form': reset_pass_form,
                'user': user
            })

#*****************************************************************************************************************************

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))

#*****************************************************************************************************************************