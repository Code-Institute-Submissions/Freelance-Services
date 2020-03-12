from django.http import HttpResponse
from django.shortcuts import render

from .models import Service
# Create your views here.

def service_list(request):
    services = Service.objects.all()
    output = ', '.join([str(service) for service in services])
    return HttpResponse(output)


