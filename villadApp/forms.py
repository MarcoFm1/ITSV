from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from villadApp import models

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    dni = forms.IntegerField()
	

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'dni']

