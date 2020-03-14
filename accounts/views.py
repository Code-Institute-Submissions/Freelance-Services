from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
# Create your views here.


def logout(request):
    """Logs the user out"""
    auth.logout(request)
    messages.success(request, "You have been succesfully logged out")
    return redirect(reverse('service'))

