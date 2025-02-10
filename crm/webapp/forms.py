from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})