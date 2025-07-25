from itertools import count

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from account_module.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/حذف نشده')

    def __str__(self):
        return f'({self.title} - {self.url_title})'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'



class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام برند', db_index=True)
    url_title = models.CharField(max_length=300, verbose_name='نام در url', db_index=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.title



class Product(models.Model):

    title = models.CharField(max_length=300, verbose_name='نام محصول')

    brand = models.ForeignKey(ProductBrand, null=True, blank=True, on_delete=models.CASCADE, verbose_name='برند')

    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')

    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')

    price = models.IntegerField(default=0, verbose_name='قیمت')

    short_description = models.CharField(max_length=360, null=True, db_index=True, verbose_name='توضیحات کوتاه')

    description = models.TextField(db_index=True, verbose_name='توضیحات اصلی')

    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    slug = models.CharField(default='', null=False, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در Url')
    # slug = models.SlugField(default='', null=False, validators=[], db_index=True, blank=True, max_length=200, unique=True, verbose_name='عنوان در Url')

    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/حذف نشده')


    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:  # فقط اگر مقدار slug خالی بود، مقدار جدید تولید شود
            base_slug = slugify(self.title, allow_unicode=True)
            slug = base_slug
            counter = 1

            while Product.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'



class ProductTag(models.Model):
    caption = models.CharField(max_length=300, verbose_name='عنوان', db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'



class ProductVisit(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_visits',
                                verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return f"{self.product} ({self.ip})"

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'



class ProductGallery(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/product-gallery', verbose_name='تصویر')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'گالری تصاویر'