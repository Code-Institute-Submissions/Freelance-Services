from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('service_list', views.service_list, name='service')
]