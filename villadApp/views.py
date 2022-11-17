from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ITS(request):
    return render(request,'../templates/villadApp/main.html')

def LOGIN(request):
    return render(request,'../templates/villadApp/login.html')

def PROFILE(request,tipo,nombre):
    if tipo == 'estudiante':
        print('ESTUDIA DJANGO NOOOOOOOOOOOOOOOOOOOOOO')
    else:
        print('SE RASCA LOS HUEVOS')
    return render(request,'../templates/villadApp/profile.html')
