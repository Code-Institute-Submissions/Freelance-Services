from django.http import HttpResponse
from django.shortcuts import render

from .models import Service
# Create your views here.

def service_list(request):
    services = Service.objects.all()
    close_div = [] # use to store the amount of closing div tags required.
    while (len(close_div) < len(services) % 3):
        close_div.append(1)
    return render(request, 'services/service_list.html', {'services': services}, {'close_div':close_div})


