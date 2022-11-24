from django.contrib import admin
from .models import *
# Register your models here.

#cosicas
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("curso", "materia") #Muestra nombre precio y stock en la pagina
    list_filter = ("curso", "materia") #Agrega un filtro de datos a la derecha
    search_fields = ["materia"] #Agrega un buscador por nombre

    fieldsets = (
        ('Nuevo producto', { #"Titulo" a la seccion de add
            "fields": ("curso", "materia") #Adjunta segun lo que pongas aca, si queres 
        }),                                         #poner por ejemplo otra seccion, pones otro "fields"
    )


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("curso") #Muestra nombre precio y stock en la pagina
    list_filter = ("curso") #Agrega un filtro de datos a la derecha
    search_fields = ["curso"] #Agrega un buscador por nombre

    fieldsets = (
        ('Nuevo producto', { #"Titulo" a la seccion de add
            "fields": ("curso") #Adjunta segun lo que pongas aca, si queres 
        }),                                         #poner por ejemplo otra seccion, pones otro "fields"
    )




#cosas
admin.site.register(Anio)
admin.site.register(Division)
admin.site.register(Especialidad)
admin.site.register(DiasSemana)
# materia cosas
admin.site.register(Modulo)
admin.site.register(Materia)
admin.site.register(ContenidosMateria)
# cursos y cosas
admin.site.register(Curso)
admin.site.register(Cronograma)
admin.site.register(CronogramaDia)
admin.site.register(MateriaHorario)
admin.site.register(Temario)
# personas
admin.site.register(Autorizado)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Tutor)
admin.site.register(RelacionAT)
admin.site.register(EncargadoFaltas)
# faltas
admin.site.register(Asistencia)
admin.site.register(Falta)
