"""freelance_services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from accounts.views import logout, login, register, profile_page
from services.views import all_services
from home.views import index
from checkout.views import checkout
from basket.views import view_basket, add_to_basket, adjust_basket
from .settings import MEDIA_ROOT
from django.views import static


urlpatterns = [
    path("", index, name='index'),   
    path('checkout', checkout, name='checkout'),
    path('admin/', admin.site.urls),
    path('services/', all_services, name='services'),
    path('accounts/', include('accounts.urls')),
    path('basket/', include('basket.urls')),
    re_path(r'^accounts/logout/$', logout, name="logout"),
    re_path(r'^accounts/login/$', login, name="login"),
    re_path(r'^accounts/register/$', register, name="register"),
    re_path(r'^accounts/profile/$', profile_page, name="profile"),
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
