from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required # Needed for login_required decorator
from django.contrib.auth.models import User
from accounts.forms import LoginForm, RegisterForm
# Create your views here.

@login_required # Ensures user is logged in before executing 
def logout(request):
    """Logs the user out"""
    auth.logout(request)
    messages.success(request, "You have been succesfully logged out")
    return redirect(reverse('index'))

def login(request):
    """Return log in page"""
    if request.user.is_authenticated:
         return redirect(reverse('service'))
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password']) 
            if user: 
                auth.login(user=user, request=request)
                messages.success(request, 'You have logged in successfully')
                return redirect(reverse('index')) #TODO: When orders page is created redirect to orders. 
            else: 
                login_form.add_error(None, 'Your username or password is incorrect')
    else:
        login_form = LoginForm()
    return render(request, 'accounts/login.html', {"login_form": login_form})


def register(request):
    """Return register page"""
    if request.user.is_authenticated:
        return redirect(reverse('index')) #TODO: When orders page is created redirect to orders.

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1']) 
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered')
                return redirect(reverse('index')) #TODO: When orders page is created redirect to orders.
            else: 
                messages.error(request, 'Unable to register your account at this time')
    else:
        register_form = RegisterForm()
    return render(request, 'accounts/register.html', {"register_form": register_form})

def profile_page(request):
    """A page that displays the profile of the user"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'accounts/profile.html', {"profile": user})