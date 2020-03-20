from django.urls import path, re_path, include
from .views import all_services

urlpatterns = [
    path('services', all_services, name='services')
]