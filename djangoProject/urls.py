from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import contact_module

urlpatterns = [
    path('', include('home_module.urls') ),
    path('', include('account_module.urls') ),
    path('contact-us/', include('contact_module.urls') ),
    path('articles/', include('article_module.urls') ),
    path('create-profile/', contact_module.views.CreateProfileView.as_view(), name='create_profile_page'),
    path('profiles/', contact_module.views.ProfilesView.as_view(), name='profiles_page'),
    path('admin/', admin.site.urls, name='admin'),
    path('products/', include("product_module.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
