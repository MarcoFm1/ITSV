from django.db import models


# Create your models here.
# COSAS PARA MARTA LA SECRETARIA DE 150 AÑOS
class Anios(models.Model):
    anio = models.IntegerField(db_column='ANIO', max_length=1)  # Field name made lowercase.

    def __str__(self) -> str:
        return str(self.anio)

class Divisiones(models.Model):
    division = models.CharField(db_column='DIVISION', max_length=1)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.division

class Especialidades(models.Model):
    especialidad = models.CharField(db_column='ESPECIALIDADES', max_length=30)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.especialidad

class DiasSemana(models.Model):
    dia = models.CharField(db_column='DIA', max_length=30)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.dia
# Persona
class Personas(models.Model):
    dni = models.CharField(db_column='DNI TUTOR', max_length=7)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE TUTOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO TUTOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO TUTOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL TUTOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self) -> str:
        return self.nombre
# Materias
class Materias(models.Model):
    nombre = models.CharField(db_column='NOMBRE', max_length=35, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=150, blank=True, null=True)  # Field name made lowercase.
    objetivos = models.CharField(db_column='OBJETIVOS', max_length=150, blank=True, null=True)  # Field name made lowercase.
    contenidos = models.CharField(db_column='CONTENIDOS', max_length=150, blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.nombre

class HorariosMaterias(models.Model):
    hora_inicio = models.TimeField(db_column='HORA INICIO')  # Field name made lowercase.
    hora_final = models.TimeField(db_column='HORA FINAL')  # Field name made lowercase.CASCADE
    materia = models.ForeignKey(Materias, models.DO_NOTHING, db_column='MATERIA', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return f'{self.materia} {self.hora_inicio} {self.hora_final}'

# Curso

class Cursos(models.Model):  
    anio_creacion = models.DateField(db_column='CREACION_HORARIO')
    anio = models.ForeignKey(Anios, models.DO_NOTHING, db_column='ANIO', blank=True, null=True)  # Field name made lowercase.
    division = models.ForeignKey(Divisiones, models.DO_NOTHING, db_column='DIVISION', blank=True, null=True)  # Field name made lowercase.
    especialidad = models.ForeignKey(Especialidades, models.DO_NOTHING, db_column='ESPECIALIDAD', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return f'{self.anio} ° {self.division}'


class MateriasXCursos(models.Model):
    anio_creacion = models.DateField(db_column='CREACION_HORARIO')
    materia = models.ForeignKey(Materias, models.DO_NOTHING, db_column='MATERIA', blank=True, null=True)  # Field name made lowercase.
    curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='CURSO', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self) -> str:
        return f'{self.curso} {self.materia.nombre}'

class CronogramaCursos(models.Model):
    anio_creacion = models.DateField(db_column='CREACION_HORARIO')
    dia = models.ForeignKey(DiasSemana, models.DO_NOTHING, db_column='DIA', blank=True, null=True)
    curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='CURSO', blank=True, null=True)  # Field name made lowercase.
    horarios_materia = models.ForeignKey(HorariosMaterias, models.DO_NOTHING, db_column='HORARIO_MATERIA', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.curso} {self.dia}'

# alumno
