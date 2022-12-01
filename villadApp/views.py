from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def ITS(request):
    return render(request,'../templates/villadApp/main.html')

def LOGIN(request):
    return render(request,'../templates/villadApp/login.html')

def ASISTENCIA(request):
    cursosEncargado = Curso.objects.all().filter(id=1)
    response = {"lista": Alumno.objects.all().filter(curso = cursosEncargado[0])}
    return render(request,'../templates/villadApp/asistencia.html', response)

def PROFILE(request,tipo,nombre):
    
    if tipo == 'estudiante':
        estudiante = Alumno.objects.all().get(nombre = nombre)
        materia_horario = MateriaHorario.objects.all().filter(dia__cronograma__curso = estudiante.curso)
        rol = 'Estudiante'

        nombre_final = ''
        for i in nombre:
            if i.isupper():
                nombre_final += f' {i}'
            else:
                nombre_final += f'{i}'
    else:
        nombre_final = nombre
        

    nombre = nombre_final
    
    modulos_materias = {}
    for i in materia_horario:
        if i.modulo.orden in modulos_materias:
            modulos_materias[i.modulo.orden][f'{i.dia.dia}'] = i.materia.nombre 
        else:
            modulos_materias[i.modulo.orden] = {f'{i.dia.dia}':i.materia.nombre}
            
    response = {'nombre':nombre,'estudiante':estudiante,'rol':rol,'modulos':modulos_materias}
    return render(request,'../templates/villadApp/profile.html',response)
