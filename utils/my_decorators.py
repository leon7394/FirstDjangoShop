from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import urlencode


def permission_checker_decorator(func):
    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated and request.user.is_superuser:
            return func(request, *args, **kwargs)

        if request.user.is_authenticated and not request.user.is_superuser:
            return HttpResponseForbidden()
        else:
            current_url = request.get_full_path()
            login_url = reverse('login_page')
            query_string = urlencode({'next': current_url})
            redirect_url = f"{login_url}?{query_string}"
            return redirect(redirect_url)
    return wrapper