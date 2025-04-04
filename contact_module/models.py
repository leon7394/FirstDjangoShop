from django.db import models
import jdatetime
import pytz


class ContactUs(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    title = models.CharField(max_length=300, verbose_name='عنوان')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def get_shamsi_date(self):
        tehran_tz = pytz.timezone('Asia/Tehran')
        tehran_time = self.created_date.astimezone(tehran_tz)

        shamsi_date = jdatetime.datetime.fromgregorian(datetime=tehran_time)

        persian_months = {
            "Farvardin": "فروردین", "Ordibehesht": "اردیبهشت", "Khordad": "خرداد",
            "Tir": "تیر", "Mordad": "مرداد", "Shahrivar": "شهریور",
            "Mehr": "مهر", "Aban": "آبان", "Azar": "آذر",
            "Dey": "دی", "Bahman": "بهمن", "Esfand": "اسفند"
        }

        month_fa = persian_months[shamsi_date.strftime('%B')]
        return shamsi_date.strftime(f'%d {month_fa} %Y - %H:%M')

    get_shamsi_date.short_description = "تاریخ شمسی"

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')