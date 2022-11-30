from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import CreateUserForm

from django.contrib import messages

# Create your views here.

def ITS(request):
    return render(request,'../templates/villadApp/main.html')

def REGISTER(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Registrado correctamente: ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, '../templates/villadApp/register.html', context)


def LOGIN(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')


    context = {}
    return render(request,'../templates/villadApp/login.html', context)
