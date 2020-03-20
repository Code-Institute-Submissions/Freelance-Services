from django.http import HttpResponse
from django.shortcuts import render

from .models import Service
# Create your views here.

def all_services(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})