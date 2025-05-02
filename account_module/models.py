from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.CharField(max_length=20, unique=True, verbose_name='تصویر پروفایل', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, unique=True, verbose_name = 'کد فعال سازی ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()