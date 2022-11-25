from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Fue creada, te podes loguear')    
            return redirect('../templates/villadApp/login.html')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, '../templates/villadApp/register.html', context)

# Create your views here.

def ITS(request):
    return render(request,'../templates/villadApp/main.html')

def REGISTER(request):
    return render(request,'../templates/villadApp/register.html')

def LOGIN(request):
    return render(request,'../templates/villadApp/login.html')

def QUERY(request):
    return render(request,'../templates/villadApp/query.html')

