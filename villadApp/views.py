from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

# Create your views here.

def ITS(request):
    return render(request,'../templates/villadApp/index.html')

def LOGIN(request):
    return render(request,'../templates/villadApp/login.html')

def ASISTENCIA(request):
    return render(request,'../templates/villadApp/asistencia.html')

def PROFILE(request,tipo,nombre):
    if tipo == 'estudiante':
        estudiante = Alumno.objects.all().get(nombre = nombre)
        materia_horario = MateriaHorario.objects.all().filter(dia__cronograma__curso = estudiante.curso)

        modulos_materias = {}
        for i in materia_horario:
            if i.modulo.orden in modulos_materias:
                modulos_materias[i.modulo.orden][f'{i.dia.dia}'] = i.materia.nombre 
            else:
                modulos_materias[i.modulo.orden] = {f'{i.dia.dia}':i.materia.nombre}
        
        
        response = {'nombre':nombre,'estudiante':estudiante,'rol':tipo.title(),'modulos':modulos_materias}
        return render(request,'../templates/villadApp/profile.html',response)
    else:
        return redirect('villada')
    
def DESCRIPCION(request,objeto,elemento,atributo):
    if objeto == 'materias':
        materia = Materia.objects.all().get(nombre = elemento)
        response = {'objeto':objeto,'elemento_nombre':materia.nombre,'elemento_descripcion':f'{materia.nombre} ({materia.abreviado}) {materia.descripcion}'}
        return render(request,'../templates/villadApp/materias.html',response)
    
    elif objeto == 'modulos':
        modulo = Modulo.objects.all().get(orden = int(elemento))
        curso = Curso.objects.all().get(anio__anio = int(atributo[0]),division__division = atributo[1])
        materia_horario = MateriaHorario.objects.all().filter(dia__cronograma__curso = curso,modulo__orden = int(elemento)).order_by('dia__dia')

        modulos_materias = {}
        for i in materia_horario:
            modulos_materias[f'{i.dia.dia}'] = {'nombre':i.materia.nombre,'abreviacion':i.materia.abreviado} 
        
        response = {'objeto':objeto,'orden':modulo.orden,'sufijo':f'{modulo.orden}{modulo.sufijo}','atributo':atributo,'elemento_descripcion':modulos_materias.values()}
        return render(request,'../templates/villadApp/materias.html',response)
    
    elif objeto == 'dias':
        curso = Curso.objects.all().get(anio__anio = int(atributo[0]),division__division = atributo[1],)
        
        if elemento =='All':
            materia_horario = MateriaHorario.objects.all().filter(dia__cronograma__curso = curso).order_by('dia__dia','modulo__orden')
            
            modulos_materias = {}
            for i in materia_horario:
                if i.modulo.orden in modulos_materias:
                    modulos_materias[i.modulo.orden][f'{i.dia.dia}'] = {'nombre':i.materia.nombre,'abreviacion':i.materia.abreviado}
                else:
                    modulos_materias[i.modulo.orden] = {'orden':i.modulo,f'{i.dia.dia}':{'nombre':i.materia.nombre,'abreviacion':i.materia.abreviado}}

            response = {'objeto':objeto,'elemento':elemento,'atributo':atributo,'modulos_materia':modulos_materias}
            
        else:
            materia_horario = MateriaHorario.objects.all().filter(dia__cronograma__curso = curso, dia__dia__dia = elemento).order_by('modulo__orden')
            response = {'objeto':objeto,'elemento':elemento,'atributo':atributo,'materia_horario':materia_horario}

        return render(request,'../templates/villadApp/materias.html',response)
    else:
        return redirect('villada')
def CURSOS(request):
    return render(request,'../templates/villadApp/cursos.html')

