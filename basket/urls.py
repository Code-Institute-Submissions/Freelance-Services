from django.urls import path, re_path, include
from .views import view_basket, add_to_basket, adjust_basket

urlpatterns = [
    re_path(r'^view', view_basket, name='view_basket'),
    re_path(r'^add/(?P<id>\d+)', add_to_basket, name='add_to_basket'),
    re_path(r'^adjust/(?P<id>\d+)', adjust_basket, name='adjust_basket'),
]