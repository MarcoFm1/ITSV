from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from villadApp import models


class UserRegistrationForm(UserCreationForm):
    CHOICES = (
      (1, 'Alumno'),
      (2, 'Preceptor'),
      (3, 'Tutor'),
      
  )
    role = forms.ChoiceField(choices=CHOICES)
    dni = forms.IntegerField()
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
	

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'dni', 'email', 'password1', 'password2', 'role']

