from django.urls import path, re_path
from .views import checkout

urlpatterns = [
   path('checkout', checkout, name='checkout'),
]