from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import LoginForm
# Create your views here.


def logout(request):
    """Logs the user out"""
    auth.logout(request)
    messages.success(request, "You have been succesfully logged out")
    return redirect(reverse('service'))

def login(request):
    """Return log in page"""
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
           

            if user: 
                auth.login(user=user, request=request)
                messages.success(request, 'You have logged in successfully')
            else: 
                login_form.add_error(None, 'Your username or password is incorrect')
    else:
        login_form = LoginForm()
    return render(request, 'accounts/login.html', {"login_form": login_form})