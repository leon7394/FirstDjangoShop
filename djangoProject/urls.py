from django.contrib import admin
from django.urls import path, include
import contact_module

urlpatterns = [
    path('', include('home_module.urls') ),
    path('contact-us/', include('contact_module.urls') ),
    path('create-profile/', contact_module.views.CreateProfileView.as_view(), name='create_profile_page'),
    path('admin/', admin.site.urls, name='admin'),
    path('products/', include("product_module.urls"))
]
