from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/avatars', null=True, blank=True, verbose_name='تصویر پروفایل')
    email_active_code = models.CharField(max_length=100, unique=True, verbose_name = 'کد فعال سازی ایمیل')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.email