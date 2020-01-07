from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(min_length=2, max_length=100, label='First Name')
    last_name = forms.CharField(min_length=2, max_length=100, label='Last Name')
    #username = forms.CharField(min_length=2, max_length=50, label='User Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
