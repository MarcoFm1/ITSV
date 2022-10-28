from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ITS(request):
    return render(request,'../templates/villadApp/main.html')

def LOGIN(request):
    return render(request,'../templates/villadApp/login.html')
