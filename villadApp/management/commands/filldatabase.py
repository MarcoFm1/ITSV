from django.core.management.base import BaseCommand, CommandError
from villadApp.models import *
import datetime

class Command(BaseCommand):
    help = 'fills the database'
    print("worked?")
    def handle(self, *args, **options):
        for i in range(7):
            Anio(id=i+1, fechacreacion=datetime.date.today(), anio=i+1).save()
        
        Division(id=1, fechacreacion=datetime.date.today(), division='A').save()
        Division(id=2, fechacreacion=datetime.date.today(), division='B').save()
        Division(id=3, fechacreacion=datetime.date.today(), division='C').save()

        Especialidad(id=1, fechacreacion=datetime.date.today(), especialidad='Programacion').save()
        Especialidad(id=2, fechacreacion=datetime.date.today(), especialidad='Electronica').save()
        Especialidad(id=3, fechacreacion=datetime.date.today(), especialidad='Electromecanica').save()

        cont = 1
        for i in ['Lunes','Martes','Miercoles','Jueves','Viernes']:
            DiasSemana(id=cont, fechacreacion=datetime.date.today(), dia=i).save()
            cont +=1
        
        Modulo(id=1, fechacreacion=datetime.date.today(), sufijo='ro', hora_inicio='07:50:00', hora_final='08:30:00', orden='1').save()
        Modulo(id=2, fechacreacion=datetime.date.today(), sufijo='do', hora_inicio='08:30:00', hora_final='09:05:00', orden='2').save()
        Modulo(id=3, fechacreacion=datetime.date.today(), sufijo='ro', hora_inicio='09:25:00', hora_final='10:05:00', orden='3').save()
        Modulo(id=4, fechacreacion=datetime.date.today(), sufijo='to', hora_inicio='10:05:00', hora_final='10:45:00', orden='4').save()
        Modulo(id=5, fechacreacion=datetime.date.today(), sufijo='to', hora_inicio='10:55:00', hora_final='11:35:00', orden='5').save()
        Modulo(id=6, fechacreacion=datetime.date.today(), sufijo='to', hora_inicio='11:35:00', hora_final='12:15:00', orden='6').save()
        Modulo(id=7, fechacreacion=datetime.date.today(), sufijo='mo', hora_inicio='12:55:00', hora_final='13:25:00', orden='7').save()
        Modulo(id=8, fechacreacion=datetime.date.today(), sufijo='vo', hora_inicio='13:25:00', hora_final='14:05:00', orden='8').save()
        Modulo(id=9, fechacreacion=datetime.date.today(), sufijo='no', hora_inicio='14:05:00', hora_final='14:45:00', orden='9').save()
        Modulo(id=10, fechacreacion=datetime.date.today(), sufijo='mo', hora_inicio='14:55:00', hora_final='15:30:00', orden='10').save()
        Modulo(id=11, fechacreacion=datetime.date.today(), sufijo='vo', hora_inicio='15:30:00', hora_final='16:10:00', orden='11').save()

        Materia(id=1, fechacreacion=datetime.date.today(), abreviado='LEN', nombre='Lengua', descripcion='').save()

        ContenidosMateria(id=1, fechacreacion=datetime.date.today(), nombre='', descripcion='', materia='').save()
        self.stdout.write(self.style.SUCCESS("this worked"))