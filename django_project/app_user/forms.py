from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Имя')
    second_name = forms.CharField(max_length=30, help_text='Фамилия')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'second_name', 'password1', 'password2')

