from django.contrib import admin
from .models import Anio, Division, Especialidad, DiasSemana, Modulo, Materia, ContenidosMateria, Curso, Cronograma, CronogramaDia, MateriaHorario, Temario, Autorizado, Profesor, Alumno, Tutor, RelacionAT, EncargadoFaltas, Asistencia, Falta, ObjetivosMateria

# Register your models here.

# COSICAS


# personas
class ProfesorAdmin(admin.ModelAdmin):  
    list_display = ("dni", "nombre", "apellido", "telefono", "email") #Muestra nombre precio y stock en la pagina
    list_filter = ("dni", "nombre", "apellido") #Agrega un filtro de datos a la derecha
    search_fields = ("nombre", "apellido") #Agrega un buscador por nombre

class AlumnoAdmin(admin.ModelAdmin):  
    list_display = ("dni", "nombre", "apellido", "telefono", "email") #Muestra nombre precio y stock en la pagina
    list_filter = ("dni", "nombre", "apellido") #Agrega un filtro de datos a la derecha
    search_fields = ("nombre", "apellido") #Agrega un buscador por nombre

class TutorAdmin(admin.ModelAdmin):  
    list_display = ("dni", "nombre", "apellido", "telefono", "email") #Muestra nombre precio y stock en la pagina
    list_filter = ("dni", "nombre", "apellido") #Agrega un filtro de datos a la derecha
    search_fields = ("nombre", "apellido") #Agrega un buscador por nombre

class EncargadoFaltasAdmin(admin.ModelAdmin):  
    list_display = ("dni", "nombre", "apellido", "telefono", "email") #Muestra nombre precio y stock en la pagina
    list_filter = ("dni", "nombre", "apellido") #Agrega un filtro de datos a la derecha
    search_fields = ("nombre", "apellido") #Agrega un buscador por nombre



# materia cosas
class ModuloAdmin(admin.ModelAdmin):  
    list_display = ("fechacreacion", "hora_inicio", "hora_final", "orden") #Muestra nombre precio y stock en la pagina
    list_filter = ("fechacreacion", "hora_inicio", "hora_final", "orden") #Agrega un filtro de datos a la derecha
    search_fields = ("hora_inicio", "orden") #Agrega un buscador por nombre

class MateriaAdmin(admin.ModelAdmin):  
    list_display = ("fechacreacion", "nombre", "descripcion") #Muestra nombre precio y stock en la pagina
    list_filter = ("fechacreacion", "nombre", "descripcion") #Agrega un filtro de datos a la derecha
    search_fields = ["nombre"] #Agrega un buscador por nombre

class ContenidosMateriaAdmin(admin.ModelAdmin):  
    list_display = ("fechacreacion", "nombre", "descripcion", "materia") #Muestra nombre precio y stock en la pagina
    list_filter = ("fechacreacion", "nombre", "descripcion", "materia") #Agrega un filtro de datos a la derecha
    search_fields = ["nombre"] #Agrega un buscador por nombre



# cursos y cosas
class CursoAdmin(admin.ModelAdmin):  
    list_display = ("fechacreacion", "anio", "division", "especialidad") #Muestra nombre precio y stock en la pagina
    list_filter = ("fechacreacion", "anio", "division", "especialidad") #Agrega un filtro de datos a la derecha
    search_fields = ("anio", "division", "especialidad") #Agrega un buscador por nombre

class CronogramaAdmin(admin.ModelAdmin):  
    list_display = ("fechacreacion", "curso") #Muestra nombre precio y stock en la pagina
    list_filter = ("fechacreacion", "curso") #Agrega un filtro de datos a la derecha



#cosas
admin.site.register(Anio)
admin.site.register(Division)
admin.site.register(Especialidad)
admin.site.register(DiasSemana)
# materia cosas
admin.site.register(Modulo, ModuloAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(ContenidosMateria, ContenidosMateriaAdmin)
# cursos y cosas
admin.site.register(Curso, CursoAdmin)
admin.site.register(Cronograma, CronogramaAdmin)
admin.site.register(CronogramaDia)
admin.site.register(MateriaHorario)
admin.site.register(Temario)
admin.site.register(ObjetivosMateria)
# personas
admin.site.register(Autorizado)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(RelacionAT)
admin.site.register(EncargadoFaltas, EncargadoFaltasAdmin)
# faltas
admin.site.register(Asistencia)
admin.site.register(Falta)
