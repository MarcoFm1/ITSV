from django.db import models


# Create your models here.
# COSAS PARA MARTA LA SECRETARIA DE 150 AÑOS
class Anio(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    anio = models.IntegerField(db_column='ANIO')  # Field name made lowercase.

    def __str__(self) -> str:
        return str(self.anio)

class Division(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    division = models.CharField(db_column='DIVISION', max_length=1)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.division

class Especialidad(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    especialidad = models.CharField(db_column='ESPECIALIDADES', max_length=30)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.especialidad

class DiasSemana(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    dia = models.CharField(db_column='DIA', max_length=30)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.dia
# persona
class Persona(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    dni = models.CharField(db_column='DNI', max_length=8)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        abstract = True
# clase para materias
class Modulo(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    hora_inicio = models.TimeField(db_column='HORA INICIO')  # Field name made lowercase.
    hora_final = models.TimeField(db_column='HORA FINAL')  # Field name made lowercase.CASCADE
    orden = models.IntegerField(db_column='ORDEN')  # Field name made lowercase.
    def __str__(self) -> str:
        return f"{self.orden}: {self.hora_inicio}, {self.hora_final}"

class Materia(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    abreviado = models.CharField(db_column='ABREVIADO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    def __str__(self) -> str:
        return self.nombre

class ContenidosMateria(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='CONTENIDOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    materia = models.ForeignKey(Materia, models.DO_NOTHING, db_column='MATERIA', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return f'{self.materia} contenidos'

class ObjetivosMateria(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    nombre = models.CharField(db_column='OBJETIVOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='CONTENIDOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    materia = models.ForeignKey(Materia, models.DO_NOTHING, db_column='MATERIA', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return f'{self.materia} contenidos'

# clase para cursos

class Curso(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    anio = models.ForeignKey(Anio, models.DO_NOTHING, db_column='ANIO', blank=True, null=True)  # Field name made lowercase.
    division = models.ForeignKey(Division, models.DO_NOTHING, db_column='DIVISION', blank=True, null=True)  # Field name made lowercase.
    especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='ESPECIALIDAD', blank=True, null=True)  # Field name made lowercase.
    def __str__(self) -> str:
        return f'{self.anio} ° {self.division}, {self.especialidad}'

class Cronograma(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CURSO', blank=True, null=True)
    def __str__(self) -> str:
        return f'{self.fechacreacion.year}: {self.curso.division} ° {self.curso.division}'

class CronogramaDia(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    cronograma = models.ForeignKey(Cronograma, models.DO_NOTHING, db_column='CRONOGRAMA', blank=True, null=True)
    dia = models.ForeignKey(DiasSemana, models.DO_NOTHING, db_column='DIA', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.fechacreacion.year}: {self.dia}: {self.cronograma.curso.division} ° {self.cronograma.curso.division}'

class MateriaHorario(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    materia = models.ForeignKey(Materia, models.DO_NOTHING, db_column='MATERIA', blank=True, null=True)
    modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='MODULO', blank=True, null=True)
    dia = models.ForeignKey(CronogramaDia, models.DO_NOTHING, db_column='DIA_SEMANA', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.fechacreacion.year}: {self.dia}: {self.materia}: {self.modulo}'


class Temario(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    materia = models.ForeignKey(Materia, models.DO_NOTHING, db_column='MATERIA', blank=True, null=True)    
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CURSO', blank=True, null=True)    
    def __str__(self) -> str:
        return f'{self.curso.anio} ° {self.curso.division}: {self.materia}'
# PERSONAS DESTACADAS
class Autorizado(models.Model):
    dni = models.CharField(db_column='DNI', max_length=8)  # Field name made lowercase.
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}, {self.curso.anio}°{self.curso.division}'

class Profesor(Persona):
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CURSO', blank=True, null=True)  # Field name made lowercase.
    materia = models.ForeignKey(MateriaHorario, models.DO_NOTHING, db_column='MATERIA_ENCARGADA', blank=True, null=True)
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}, {self.curso.anio}°{self.curso.division}'
    class Meta(Persona.Meta):
        pass

class Alumno(Persona):
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CURSO', blank=True, null=True)  # Field name made lowercase.
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}, {self.curso.anio}°{self.curso.division}'
    class Meta(Persona.Meta):
        pass

class Tutor(Persona):
    def __str__(self) -> str:
        return f'tutor: {self.nombre} {self.apellido}'
    
    class Meta(Persona.Meta):
        pass

class RelacionAT(models.Model):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    tutores = models.ForeignKey(Tutor, models.DO_NOTHING, db_column='TUTORES', blank=True, null=True)  # Field name made lowercase.
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='ALUMNO', blank=True, null=True)  # Field name made lowercase.
    class Meta(Persona.Meta):
        pass

    def __str__(self) -> str:
        return f'{self.tutores} tutor de: {self.alumno}'

class EncargadoFaltas(Persona):
    fechacreacion = models.DateField(db_column="CREACION", auto_now_add=True, editable=False)
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CURSO', blank=True, null=True)  # Field name made lowercase.
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}, {self.curso.anio}°{self.curso.division}'
    class Meta(Persona.Meta):
        pass
# asistencias
class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='ALUMNO', blank=True, null=True)  # Field name made lowercase.
    materia = models.ForeignKey(MateriaHorario, models.DO_NOTHING, db_column='MATERIA', blank=True, null=True)
    dia = models.DateField(db_column='DIA', auto_now_add=True, editable=False)
    class Meta(Persona.Meta):
        pass

    def __str__(self) -> str:
        return f'dia: {self.dia} alumno: {self.alumno} materia: {self.materia}'

class Falta(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='ALUMNO', blank=True, null=True)  # Field name made lowercase.
    materia = models.ForeignKey(MateriaHorario, models.DO_NOTHING, db_column='MATERIA', blank=True, null=True)
    dia = models.DateField(db_column='DIA_FALTA', auto_now_add=True, editable=False)
    llegada = models.BooleanField(db_column='ASISTIO')
    hora_llegada = models.TimeField(db_column='HORA_LLEGADA')
    class Meta(Persona.Meta):
        pass

    def __str__(self) -> str:
        return f'dia: {self.dia} alumno: {self.alumno} materia: {self.materia} llego?: {self.llegada} hora llegada: {self.hora_llegada}'
#try