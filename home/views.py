from django.shortcuts import render
from .models import HomePage

# Create your views here.
def index(request):
    homepage = HomePage.objects.all()
    return render(request, 'home/index.html', {'homepage': homepage})