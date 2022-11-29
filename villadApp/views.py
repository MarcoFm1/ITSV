from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def ITS(request):
    return render(request,'../templates/villadApp/main.html')

def REGISTER(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, '../templates/villadApp/register.html', context)

def LOGIN(request):
    context = {}
    return render(request,'../templates/villadApp/login.html', context)

def PRUEBA():
    print('enie')