from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Anio)
admin.site.register(Division)
admin.site.register(Especialidad)
admin.site.register(DiasSemana)
admin.site.register(Alumno)
admin.site.register(Tutor)
admin.site.register(Materia)
admin.site.register(Modulo)
admin.site.register(Curso)
admin.site.register(MateriaXCurso)
admin.site.register(CronogramaCurso)
admin.site.register(RelacionAT)
admin.site.register(Falta)
admin.site.register(Asistencia)