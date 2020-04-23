from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class': 'input'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        fields = ('username', 'password')
