from django.db import models


# Create your models here.
# COSAS PARA MARTA LA SECRETARIA DE 150 AÑOS
class Anio(models.Model):
    anio = models.IntegerField(db_column='ANIO')  # Field name made lowercase.

    def __str__(self) -> str:
        return str(self.anio)

class Division(models.Model):
    division = models.CharField(db_column='DIVISION', max_length=1)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.division

class Especialidad(models.Model):
    especialidad = models.CharField(db_column='ESPECIALIDADES', max_length=30)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.especialidad

class DiasSemana(models.Model):
    dia = models.CharField(db_column='DIA', max_length=30)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.dia
# Persona
class Persona(models.Model):
    dni = models.CharField(db_column='DNI TUTOR', max_length=7)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE TUTOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO TUTOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO TUTOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL TUTOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self) -> str:
        return self.nombre
    class Meta:
        abstract = True
# Materias
class Modulo(models.Model):
    hora_inicio = models.TimeField(db_column='HORA INICIO')  # Field name made lowercase.
    hora_final = models.TimeField(db_column='HORA FINAL')  # Field name made lowercase.CASCADE
    orden = models.IntegerField(db_column='ORDEN')  # Field name made lowercase.
    def __str__(self) -> str:
        return f"{self.orden}: {self.hora_inicio}, {self.hora_final}"

class Materia(models.Model):
    nombre = models.CharField(db_column='NOMBRE', max_length=35, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=150, blank=True, null=True)  # Field name made lowercase.
    objetivos = models.CharField(db_column='OBJETIVOS', max_length=150, blank=True, null=True)  # Field name made lowercase.
    contenidos = models.CharField(db_column='CONTENIDOS', max_length=150, blank=True, null=True)  # Field name made lowercase.
    modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='DIVISION', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.nombre

# Curso

class Curso(models.Model):  
    anio_creacion = models.DateField(db_column='CREACION_HORARIO')
    anio = models.ForeignKey(Anio, models.DO_NOTHING, db_column='ANIO', blank=True, null=True)  # Field name made lowercase.
    division = models.ForeignKey(Division, models.DO_NOTHING, db_column='DIVISION', blank=True, null=True)  # Field name made lowercase.
    especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='ESPECIALIDAD', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return f'{self.anio} ° {self.division}'


class MateriaXCurso(models.Model):
    anio_creacion = models.DateField(db_column='CREACION_HORARIO')
    materia = models.ForeignKey(Materia, models.DO_NOTHING, db_column='MATERIA', blank=True, null=True)  # Field name made lowercase.
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CURSO', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self) -> str:
        return f'{self.curso} {self.materia.nombre}'

class CronogramaCurso(models.Model):
    anio_creacion = models.DateField(db_column='CREACION_HORARIO')
    dia = models.ForeignKey(DiasSemana, models.DO_NOTHING, db_column='DIA', blank=True, null=True)
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CURSO', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return f'{self.curso} {self.dia}'

# alumno
class Tutor(Persona):
    def __str__(self) -> str:
        return f'{self.materia} {self.hora_inicio} {self.hora_final}'

class Alumno(Persona):
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CURSO', blank=True, null=True)  # Field name made lowercase.
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}, {self.curso.anio}°{self.curso.division}'
    class Meta(Persona.Meta):
        pass

class RelacionAT(models.Model):
    tutores = models.ForeignKey(Tutor, models.DO_NOTHING, db_column='TUTORES', blank=True, null=True)  # Field name made lowercase.
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='ALUMNO', blank=True, null=True)  # Field name made lowercase.
    class Meta(Persona.Meta):
        pass