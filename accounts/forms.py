from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    """Form for user login"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    """Form for user login"""
    
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation",
                                widget=forms.PasswordInput)
 

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    #Form error Checking
    def clean_email(self):
        """Checks is email is already registered"""
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email already registered')
        return email

    def clean_password2(self):
        """Checks passwords match and exist"""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")

        if password1 != password2:
            raise ValidationError("Passwords must match")

        return password2

class EditProfileForm(UserChangeForm):
    """
    Form that allows users to edit their profiles. 
    """
    password = None # Stops password from appearing on form
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )