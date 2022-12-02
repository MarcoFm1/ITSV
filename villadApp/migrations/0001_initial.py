# Generated by Django 4.1 on 2022-12-02 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Alumno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                ("dni", models.CharField(db_column="DNI", max_length=8)),
                (
                    "nombre",
                    models.CharField(
                        blank=True, db_column="NOMBRE", max_length=50, null=True
                    ),
                ),
                (
                    "apellido",
                    models.CharField(
                        blank=True, db_column="APELLIDO", max_length=50, null=True
                    ),
                ),
                (
                    "telefono",
                    models.CharField(
                        blank=True, db_column="TELEFONO", max_length=10, null=True
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, db_column="EMAIL", max_length=150, null=True
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Anio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                ("anio", models.IntegerField(db_column="ANIO")),
            ],
        ),
        migrations.CreateModel(
            name="Autorizado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dni", models.CharField(db_column="DNI", max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name="Cronograma",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CronogramaDia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "cronograma",
                    models.ForeignKey(
                        blank=True,
                        db_column="CRONOGRAMA",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.cronograma",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "anio",
                    models.ForeignKey(
                        blank=True,
                        db_column="ANIO",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.anio",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DiasSemana",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                ("dia", models.CharField(db_column="DIA", max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Division",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                ("division", models.CharField(db_column="DIVISION", max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name="Especialidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "especialidad",
                    models.CharField(db_column="ESPECIALIDADES", max_length=30),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Materia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "abreviado",
                    models.CharField(
                        blank=True, db_column="ABREVIADO", max_length=4, null=True
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        blank=True, db_column="NOMBRE", max_length=35, null=True
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(
                        blank=True, db_column="DESCRIPCION", max_length=500, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MateriaHorario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "dia",
                    models.ForeignKey(
                        blank=True,
                        db_column="DIA_SEMANA",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.cronogramadia",
                    ),
                ),
                (
                    "materia",
                    models.ForeignKey(
                        blank=True,
                        db_column="MATERIA",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.materia",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Modulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "sufijo",
                    models.CharField(
                        blank=True, db_column="SUFIJO", max_length=2, null=True
                    ),
                ),
                ("hora_inicio", models.TimeField(db_column="HORA INICIO")),
                ("hora_final", models.TimeField(db_column="HORA FINAL")),
                ("orden", models.IntegerField(db_column="ORDEN")),
            ],
        ),
        migrations.CreateModel(
            name="Tutor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                ("dni", models.CharField(db_column="DNI", max_length=8)),
                (
                    "nombre",
                    models.CharField(
                        blank=True, db_column="NOMBRE", max_length=50, null=True
                    ),
                ),
                (
                    "apellido",
                    models.CharField(
                        blank=True, db_column="APELLIDO", max_length=50, null=True
                    ),
                ),
                (
                    "telefono",
                    models.CharField(
                        blank=True, db_column="TELEFONO", max_length=10, null=True
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, db_column="EMAIL", max_length=150, null=True
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Temario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "curso",
                    models.ForeignKey(
                        blank=True,
                        db_column="CURSO",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.curso",
                    ),
                ),
                (
                    "materia",
                    models.ForeignKey(
                        blank=True,
                        db_column="MATERIA",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.materia",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RelacionAT",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "alumno",
                    models.ForeignKey(
                        blank=True,
                        db_column="ALUMNO",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.alumno",
                    ),
                ),
                (
                    "tutor",
                    models.ForeignKey(
                        blank=True,
                        db_column="TUTORES",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.tutor",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Profesor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                ("dni", models.CharField(db_column="DNI", max_length=8)),
                (
                    "nombre",
                    models.CharField(
                        blank=True, db_column="NOMBRE", max_length=50, null=True
                    ),
                ),
                (
                    "apellido",
                    models.CharField(
                        blank=True, db_column="APELLIDO", max_length=50, null=True
                    ),
                ),
                (
                    "telefono",
                    models.CharField(
                        blank=True, db_column="TELEFONO", max_length=10, null=True
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, db_column="EMAIL", max_length=150, null=True
                    ),
                ),
                (
                    "curso",
                    models.ForeignKey(
                        blank=True,
                        db_column="CURSO",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.curso",
                    ),
                ),
                (
                    "materia",
                    models.ForeignKey(
                        blank=True,
                        db_column="MATERIA_ENCARGADA",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.materiahorario",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ObjetivosMateria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "nombre",
                    models.CharField(
                        blank=True, db_column="OBJETIVOS", max_length=50, null=True
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(
                        blank=True, db_column="CONTENIDOS", max_length=50, null=True
                    ),
                ),
                (
                    "anio",
                    models.ForeignKey(
                        blank=True,
                        db_column="ANIO",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.anio",
                    ),
                ),
                (
                    "materia",
                    models.ForeignKey(
                        blank=True,
                        db_column="MATERIA",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.materia",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="materiahorario",
            name="modulo",
            field=models.ForeignKey(
                blank=True,
                db_column="MODULO",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="villadApp.modulo",
            ),
        ),
        migrations.CreateModel(
            name="Falta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dia", models.DateField(auto_now_add=True, db_column="DIA_FALTA")),
                ("llegada", models.BooleanField(db_column="ASISTIO")),
                ("hora_llegada", models.TimeField(db_column="HORA_LLEGADA", null=True)),
                (
                    "alumno",
                    models.ForeignKey(
                        blank=True,
                        db_column="ALUMNO",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.alumno",
                    ),
                ),
                (
                    "materia",
                    models.ForeignKey(
                        blank=True,
                        db_column="MATERIA",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.materiahorario",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EncargadoFaltas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dni", models.CharField(db_column="DNI", max_length=8)),
                (
                    "nombre",
                    models.CharField(
                        blank=True, db_column="NOMBRE", max_length=50, null=True
                    ),
                ),
                (
                    "apellido",
                    models.CharField(
                        blank=True, db_column="APELLIDO", max_length=50, null=True
                    ),
                ),
                (
                    "telefono",
                    models.CharField(
                        blank=True, db_column="TELEFONO", max_length=10, null=True
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, db_column="EMAIL", max_length=150, null=True
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "curso",
                    models.ForeignKey(
                        blank=True,
                        db_column="CURSO",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.curso",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="curso",
            name="division",
            field=models.ForeignKey(
                blank=True,
                db_column="DIVISION",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="villadApp.division",
            ),
        ),
        migrations.AddField(
            model_name="curso",
            name="especialidad",
            field=models.ForeignKey(
                blank=True,
                db_column="ESPECIALIDAD",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="villadApp.especialidad",
            ),
        ),
        migrations.AddField(
            model_name="cronogramadia",
            name="dia",
            field=models.ForeignKey(
                blank=True,
                db_column="DIA",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="villadApp.diassemana",
            ),
        ),
        migrations.AddField(
            model_name="cronograma",
            name="curso",
            field=models.ForeignKey(
                blank=True,
                db_column="CURSO",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="villadApp.curso",
            ),
        ),
        migrations.CreateModel(
            name="ContenidosMateria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fechacreacion",
                    models.DateField(auto_now_add=True, db_column="CREACION"),
                ),
                (
                    "nombre",
                    models.CharField(
                        blank=True, db_column="NOMBRE", max_length=50, null=True
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(
                        blank=True, db_column="CONTENIDOS", max_length=50, null=True
                    ),
                ),
                (
                    "anio",
                    models.ForeignKey(
                        blank=True,
                        db_column="ANIO",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.anio",
                    ),
                ),
                (
                    "materia",
                    models.ForeignKey(
                        blank=True,
                        db_column="MATERIA",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.materia",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Asistencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dia", models.DateField(auto_now_add=True, db_column="DIA")),
                (
                    "alumno",
                    models.ForeignKey(
                        blank=True,
                        db_column="ALUMNO",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.alumno",
                    ),
                ),
                (
                    "materia",
                    models.ForeignKey(
                        blank=True,
                        db_column="MATERIA",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="villadApp.materiahorario",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="alumno",
            name="curso",
            field=models.ForeignKey(
                blank=True,
                db_column="CURSO",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="villadApp.curso",
            ),
        ),
        migrations.AddField(
            model_name="alumno",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
