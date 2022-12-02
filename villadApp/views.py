from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import *
from .decorator import unauthenticated_user, allowed_users, admin
from .forms import CreateUserForm
from .models import *

# Create your views here.

def ITS(request):
    return render(request,'../templates/villadApp/index.html')

@unauthenticated_user
def REGISTER(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'Alumno')
            user.groups.add(group)

            Alumno.objects.create(user = user)

            messages.success(request, 'Registrado correctamente: ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, '../templates/villadApp/register.html', context)

@unauthenticated_user
def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('villada')
        else:
            messages.info(request, 'Nombre o Token incorrectos')
    context = {}
    return render(request,'../templates/villadApp/login.html', context)


@login_required(login_url='login')
@admin
def ASISTENCIA(request):
    if request.method == 'POST':
        return redirect('asistencia')
    cursosEncargado = Curso.objects.all().filter(id=1)
    response = {"lista": Alumno.objects.all().filter(curso = cursosEncargado[0])}
    return render(request,'../templates/villadApp/asistencia.html', response)


@allowed_users(allowed_roles=['Alumno'])
@login_required(login_url='login')
def PROFILE(request, tipo, nombre):
    if tipo == 'estudiante':
        estudiante = Alumno.objects.all().get(nombre = nombre)
        materia_horario = MateriaHorario.objects.all().filter(dia__cronograma__curso = estudiante.curso)
        modulos_materias = {}
        for i in materia_horario:
            if i.modulo.orden in modulos_materias:
                modulos_materias[i.modulo.orden][f'{i.dia.dia}'] = {'nombre':i.materia.nombre,'abreviacion':i.materia.abreviado}
            else:
                modulos_materias[i.modulo.orden] = {'orden':i.modulo,f'{i.dia.dia}':{'nombre':i.materia.nombre,'abreviacion':i.materia.abreviado}}

        response = {'estudiante':estudiante,'rol':tipo.title(),'modulos_materia':modulos_materias,'objeto':'dias','elemento':'All','atributo':f'{estudiante.curso.anio}{estudiante.curso.division}'}
        return render(request,'../templates/villadApp/profile.html',response)
    else:
        return redirect('villada')


@login_required(login_url='login')
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

def CURSO(request,año,divicion):
    curso = Curso.objects.all().get(anio__anio = int(año),division__division = divicion)
    materia_horario = MateriaHorario.objects.all().filter(dia__cronograma__curso = curso).order_by('materia')
    alumnos = Alumno.objects.all().filter(curso = curso).order_by('apellido','nombre')
    materias = []
    for i in materia_horario:
        if i.materia not in materias:
            materias.append(i.materia)
    
    response = {'curso':curso,'materias':materias,'alumnos':alumnos,'curso_alumnos':f'{curso.anio}{curso.division}'}
    return render(request,'../templates/villadApp/curso.html',response)
    
def HOME(request):
    return render(request,'../templates/villadApp/cursos.html')

def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('villada')
        else:
            messages.info(request, 'Nombre o Token incorrectos')

    context = {}
    return render(request,'../templates/villadApp/login.html', context)


def LOGOUT(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def CURSOS(request):
    cursos = [1,2,3,4,5,6,7]
    response = {'cursos':cursos}
    return render(request,'../templates/villadApp/cursos.html',response) 
