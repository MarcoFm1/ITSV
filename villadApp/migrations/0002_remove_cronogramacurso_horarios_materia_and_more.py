# Generated by Django 4.1.3 on 2022-11-17 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('villadApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cronogramacurso',
            name='horarios_materia',
        ),
        migrations.DeleteModel(
            name='HorariosMateria',
        ),
    ]
