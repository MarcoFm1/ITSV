from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ITS(request):
    return render(request,'../templates/villadApp/main.html')

def LOGIN(request):
    return render(request,'../templates/villadApp/login.html')

def PROFILE(request,tipo,nombre):
    
    if tipo == 'estudiante':
        nombre_final = ''
        for i in nombre:
            if i.isupper():
                nombre_final += f' {i}'
            else:
                nombre_final += f'{i}'
    else:
        print('SE RASCA LOS HUEVOS')
    
    nombre = nombre_final
    response = {'nombre':nombre}
    return render(request,'../templates/villadApp/profile.html',response)
