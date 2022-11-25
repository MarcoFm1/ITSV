from django.contrib import admin
from .models import *
# Register your models here.
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
admin.site.register(ObjetivosMateria)
# personas
admin.site.register(Autorizado)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Tutor)
admin.site.register(RelacionAT)
admin.site.register(EncargadoFaltas)
# faltas
admin.site.register(Asistencia)
admin.site.register(Falta)
