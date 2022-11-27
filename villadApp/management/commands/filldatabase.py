from django.core.management.base import BaseCommand, CommandError
from villadApp.models import *
import datetime

class Command(BaseCommand):
    
    
    help = 'fills the database'
    print("worked?")
    def handle(self, *args, **options):
        anios = {}
        divisiones = {}
        especialidades = {}
        diasSemanas = {}
        modulos = {}
        materias = {}
        contenidosMaterias = {}
        cursos = {}
        cronogramas = {}
        cronogramasDias = {}

        for i in range(7):
            anios[(f"{i+1}")] = Anio(id=i+1, fechacreacion=datetime.date.today(), anio=i+1)
        
        divisiones["A"] = Division(id=1, fechacreacion=datetime.date.today(), division='A')
        divisiones["B"] = Division(id=2, fechacreacion=datetime.date.today(), division='B')
        divisiones["C"] = Division(id=3, fechacreacion=datetime.date.today(), division='C')
        
        especialidades["P"] = Especialidad(id=1, fechacreacion=datetime.date.today(), especialidad='Programacion')
        especialidades["E"] = Especialidad(id=2, fechacreacion=datetime.date.today(), especialidad='Electronica')
        especialidades["EL"] = Especialidad(id=3, fechacreacion=datetime.date.today(), especialidad='Electromecanica')
        especialidades["VOID"] = Especialidad(id=4, fechacreacion=datetime.date.today(), especialidad='----')


        cont = 1
        for i in ['Lunes','Martes','Miercoles','Jueves','Viernes']:
            diasSemanas[str(cont)] = DiasSemana(id=cont, fechacreacion=datetime.date.today(), dia=i)
            cont += 1
        for i in diasSemanas:
            print(diasSemanas[i])
        
        modulos["1"] = Modulo(id=1, fechacreacion=datetime.date.today(), sufijo='ro', hora_inicio='07:50:00', hora_final='08:30:00', orden='1')
        modulos["2"] = Modulo(id=2, fechacreacion=datetime.date.today(), sufijo='do', hora_inicio='08:30:00', hora_final='09:05:00', orden='2')
        modulos["3"] = Modulo(id=3, fechacreacion=datetime.date.today(), sufijo='ro', hora_inicio='09:25:00', hora_final='10:05:00', orden='3')
        modulos["4"] = Modulo(id=4, fechacreacion=datetime.date.today(), sufijo='to', hora_inicio='10:05:00', hora_final='10:45:00', orden='4')
        modulos["5"] = Modulo(id=5, fechacreacion=datetime.date.today(), sufijo='to', hora_inicio='10:55:00', hora_final='11:35:00', orden='5')
        modulos["6"] = Modulo(id=6, fechacreacion=datetime.date.today(), sufijo='to', hora_inicio='11:35:00', hora_final='12:15:00', orden='6')
        modulos["7"] = Modulo(id=7, fechacreacion=datetime.date.today(), sufijo='mo', hora_inicio='12:55:00', hora_final='13:25:00', orden='7')
        modulos["8"] = Modulo(id=8, fechacreacion=datetime.date.today(), sufijo='vo', hora_inicio='13:25:00', hora_final='14:05:00', orden='8')
        modulos["9"] = Modulo(id=9, fechacreacion=datetime.date.today(), sufijo='no', hora_inicio='14:05:00', hora_final='14:45:00', orden='9')
        modulos["10"] = Modulo(id=10, fechacreacion=datetime.date.today(), sufijo='mo', hora_inicio='14:55:00', hora_final='15:30:00', orden='10')
        modulos["11"] = Modulo(id=11, fechacreacion=datetime.date.today(), sufijo='vo', hora_inicio='15:30:00', hora_final='16:10:00', orden='11')

        materias["LEN"] = Materia(id=1, fechacreacion=datetime.date.today(), abreviado='LEN', nombre='Lengua y Literatura', descripcion='Materia donde se estudia la lengua castellana y las distintas formas de comunicar ideas. La Literatura es una fuente de disfrute, de conocimientos a través de una mirada estética, de juego con el lenguaje, de valoración de aspectos verbales en circunstancias concretas y debe respetarse desde esta perspectiva. La lengua representa una herramienta fundamental para la interacción social.')
        materias["MAT"] = Materia(id=2, fechacreacion=datetime.date.today(), abreviado='MAT', nombre='Matematica', descripcion='La matemática es la ciencia deductiva que se dedica al estudio de las propiedades de los entes abstractos y de sus relaciones. Esto quiere decir que las matemáticas operan con números, símbolos, figuras geométricas, etc. La calculadora es un dispositivo muy útil en el ámbito de las matemáticas.')
        materias["PRG"] = Materia(id=3, fechacreacion=datetime.date.today(), abreviado='PRG', nombre='Programacion', descripcion='Materia donde se estudia la Progrmacion, entendida como: La programación se guía por una serie de normas y un conjunto de órdenes, instrucciones y expresiones que tienden a ser semejantes a una lengua natural acotada. Por lo cual recibe el nombre de lenguaje de programación. Y así como en los idiomas también en la informática existen diversos lenguajes de programación.')
        materias["ING"] = Materia(id=4, fechacreacion=datetime.date.today(), abreviado='ING', nombre='Ingles', descripcion='Materia donde se estudia la idioma extranjero: Ingles. En este espacio se espera mejorar las habilidades lingüísticas de los alumnos y permitirles entender uno de los idiomas más hablado en todo el mundo.')
        materias["CP"] = Materia(id=5, fechacreacion=datetime.date.today(), abreviado='CP', nombre='Ciudadania y Partarticipacion', descripcion='La Ciencia Política es una ciencia social que se aboca al estudio y el análisis de las relaciones de poder, implícitas o explícitas, entre la autoridad y los individuos, los grupos, y las organizaciones; y las estructuras, procedimientos y procesos a través de los cuales se llega a las decisiones políticas')
        materias["FVT"] = Materia(id=6, fechacreacion=datetime.date.today(), abreviado='FVT', nombre='Formacion para Vida y Trabajo', descripcion='es un espacio curricular de la escuela secundaria que tiende a generar y fortalecer vínculos entre los saberes escolares y extraescolares, a través de la participación activa y comprometida de los jóvenes en su comunidad.')
        materias["EF"] = Materia(id=7, fechacreacion=datetime.date.today(), abreviado='EF', nombre='Educacion Fisica', descripcion='Educación física es una disciplina que se centra en diferentes movimientos corporales para perfeccionar, controlar y mantener la salud mental y física del ser humano.')
        materias["BIO"] = Materia(id=8, fechacreacion=datetime.date.today(), abreviado='BIO', nombre='Biologia', descripcion='La Biología estudia los seres vivos de manera integral, desde el nivel molecular hasta como integrante de los ecosistemas, a fin de conocer su estructura, función, diversidad, origen, evolución, e interrelaciones.')
        materias["QUI"] = Materia(id=9, fechacreacion=datetime.date.today(), abreviado='QUI', nombre='Quimica', descripcion='La química es una ciencia que tiene por finalidad no sólo descubrir, sino también, y sobre todo, crear, ya que es el arte de hacer compleja la materia. Para captar la lógica de la reciente evolución de la química, hay que retroceder en el tiempo y dar un salto atrás de unos cuatro mil millones de años.')
        materias["HIS"] = Materia(id=10, fechacreacion=datetime.date.today(), abreviado='HIS', nombre='Historia', descripcion='La historia es una ciencia que nos permite conocer ese pasado para entender el presente que vivimos y construir nuestro futuro. Una de las principales razones por las que es importante estudiar historia en la actualidad es para entender el cambio de la sociedad actual y cómo surge la sociedad en la que vivimos.')
        materias["GEO"] = Materia(id=11, fechacreacion=datetime.date.today(), abreviado='GEO', nombre='Geografia', descripcion='Ciencia que estudia y describe la superficie de la Tierra en su aspecto físico, actual y natural, o como lugar habitado por la humanidad.')
        materias["FCR"] = Materia(id=12, fechacreacion=datetime.date.today(), abreviado='FCR', nombre='Formacion Cristiana', descripcion='La formación es un itinerario o proceso continuo, que abarca toda la vida del cristiano, cualquiera sea la función que cumpla en la Iglesia. Puede caracterizarse como una tarea permanente, integral y sistemática orientada a la maduración en la fe y el descubrimiento cada vez más claro de la propia vocación, a fin de vivirla en el cumplimiento de la misión.')
        materias["EA"] = Materia(id=13, fechacreacion=datetime.date.today(), abreviado='EA', nombre='Educacion Artistica', descripcion='La educación artística es un método de enseñanza que, mediante acciones y actividades artísticas (pintura, teatro, danza, música, fotografía, etc.), quiere contribuir al aprendizaje cultural, emocional y social de los estudiantes, a la vez que fomentar el desarrollo de ciertas habilidades que les resultarán muy útiles')
        materias["PSIC"] = Materia(id=14, fechacreacion=datetime.date.today(), abreviado='PSIC', nombre='Psicologia', descripcion='La psicología es la ciencia que estudia los procesos mentales. La palabra proviene del griego: psico- (alma o actividad mental) y -logía (estudio). Esta disciplina analiza las tres dimensiones de los mencionados procesos: cognitiva, afectiva y conductual.')
        materias["FILO"] = Materia(id=15, fechacreacion=datetime.date.today(), abreviado='FILO', nombre='Filosofia', descripcion='Estudia el planteamiento histórico de los razonamientos teóricos y reflexiones que fundamentan principalmente las acciones humanas, considerando tanto sus pensamientos como conocimientos. Para ello, necesitarás capacidad de análisis, curiosidad científica, espíritu crítico y argumentativo.')
        materias["DT"] = Materia(id=16, fechacreacion=datetime.date.today(), abreviado='DT', nombre='Dibujo Tecnico', descripcion='El dibujo técnico engloba trabajos como bosquejo y/o croquis, esquemas, diagramas, planos eléctricos y electrónicos, representaciones de todo tipo de elementos mecánicos, planos de arquitectura, urbanismo, etc, resueltos mediante el auxilio de conceptos geométricos, donde son aplicadas las matemáticas, la geometría')
        materias["ET"] = Materia(id=17, fechacreacion=datetime.date.today(), abreviado='ET', nombre='Educacion Tecnologica', descripcion='Principalmente se trata de mejorar e innovar los procesos básicos de enseñanza y aprendizaje. Estos instrumentos tecnológicos permiten la creación de ciertos contenidos que son conocidos como medios educativos.')
        materias["LM"] = Materia(id=18, fechacreacion=datetime.date.today(), abreviado='LM', nombre='Logica Matematica', descripcion='La lógica matemática es la disciplina que trata de métodos de razonamiento. En un nivel elemental, la lógica proporciona reglas y técnicas para determinar si es o no valido un argumento dado.')
        materias["TL"] = Materia(id=19, fechacreacion=datetime.date.today(), abreviado='TL', nombre='Taller Laboratorio', descripcion='Es el espacio de trabajo en el que se realiza un proceso de enseñanza aprendizaje, con objetivos académicos. Para que el estudiante desarrolle habilidades, actitudes y aptitudes que complementan los conocimientos y la capacitación para el desempeño laboral o profesional.')
        materias["IA"] = Materia(id=20, fechacreacion=datetime.date.today(), abreviado='IA', nombre='Informatica Aplicada', descripcion='Es la ciencia que estudia el procesamiento automático de información mediante dispositivos electrónicos y sistemas computacionales. Los sistemas informáticos deben contar con la capacidad de cumplir tres tareas básicas: entrada (captación de la información),procesamiento y salida (transmisión de los resultados).')
        materias["EP"] = Materia(id=21, fechacreacion=datetime.date.today(), abreviado='EP', nombre='Economia y Produccion', descripcion='Producción: En economía, producir es crear un bien o un servicio con un valor económico. Distribución: Es cuando se hace entrega de una mercadería. Comercialización: Es poner en venta un producto. Consumo: Es cuando utilizamos bienes o servicios para satisfacer necesidades o deseos.')
        materias["EI"] = Materia(id=22, fechacreacion=datetime.date.today(), abreviado='EI', nombre='Electronica Industrial', descripcion='El sector industrial de la electrónica está enfocado en el desarrollo y reparación de productos cuya función principal es procesar algún tipo de información.')
        materias["ELEC"] = Materia(id=23, fechacreacion=datetime.date.today(), abreviado='ELEC', nombre='Electronica', descripcion='La electrónica es una disciplina técnica y científica, está a su vez se deriva de la física, la cual consiste en aprovechar la conducta de las cargas eléctricas utilizando aparatos electrónicos y dispositivos como semiconductores.')
        materias["ERM"] = Materia(id=24, fechacreacion=datetime.date.today(), abreviado='ERM', nombre='Estatica y Res. de Materiales', descripcion='La resistencia de materiales clásica es una disciplina de la ingeniería mecánica, la ingeniería estructural, la ingeniería civil y la ingeniería de materiales que estudia la mecánica de sólidos deformables mediante modelos simplificados.')
        materias["IE"] = Materia(id=25, fechacreacion=datetime.date.today(), abreviado='IE', nombre='Informatica Electronica', descripcion='La Informática Electrónica es una materia cuyo desarrollo se sustenta en el uso y aplicación del lenguaje de programación C (y C++) en la electrónica.')
        materias["INSE"] = Materia(id=26, fechacreacion=datetime.date.today(), abreviado='INSE', nombre='Instalaciones Electricas', descripcion='La instalación eléctrica es el conjunto de circuitos eléctricos con el objetivo de conducir y distribuir la corriente eléctrica desde su punto de origen (servicio eléctrico) hasta la ultima salida eléctrica. Las instalaciones eléctricas se pueden clasificar según la tensión y según el uso.')
        materias["INSM"] = Materia(id=27, fechacreacion=datetime.date.today(), abreviado='INSM', nombre='Instrumental y Medicion', descripcion='Los métodos instrumentales son métodos analíticos que se basan el la medida de las propiedades físicas de los analitos (conductividad, potencial de electrodo, absorción o emisión de luz, relación carga/masa, fluorescencia,…) para: La determinación cuantitativa o cualitativa de los analitos : métodos no separativos.')
        materias["MIEE"] = Materia(id=28, fechacreacion=datetime.date.today(), abreviado='MIEE', nombre='Maq. Instal. Elec. Electron.', descripcion='No encontre una descripcion de esta materia: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla elementum enim non erat iaculis vestibulum. Curabitur malesuada eros quis urna cursus mollis. Cras sodales non neque ac ornare. Ut iaculis libero quis est interdum gravida. Aenean quis quam nisi. Donec maximus sagittis ligula eu suscipit. Nullam purus augue, dignissim a felis in.')
        materias["MJAE"] = Materia(id=29, fechacreacion=datetime.date.today(), abreviado='MJAE', nombre='Marco Jurid. Act. Empresarial', descripcion='En general, un marco legal es el conjunto de reglas que determinan el alcance y el tipo de participación en una entidad.')
        materias["MIE"] = Materia(id=30, fechacreacion=datetime.date.today(), abreviado='MIE', nombre='Mat. de Insumo Electronico', descripcion='La industria electrónica utiliza una variedad de metales, plásticos, materias primas y productos químicos. Algunos de los metales más comunes incluyen cobre, litio, estaño, plata, oro, níquel y aluminio.')
        materias["ME"] = Materia(id=31, fechacreacion=datetime.date.today(), abreviado='ME', nombre='Mediciones Electricas', descripcion='Materia donde se estudia: La unidad básica en electricidad es el Amperio (A), que expresa la cantidad de corriente eléctrica (I) que circula por un conductor.')
        materias["SEAM"] = Materia(id=32, fechacreacion=datetime.date.today(), abreviado='SEAM', nombre='Sist. Elect. Analog. y Med.', descripcion='Una señal analógica es continua, y puede tomar infinitos valores. Una señal digital es discontinua, y sólo puede tomar dos valores o estados: 0 y 1, que pueden ser impulsos eléctricos de baja y alta tensión, interruptores abiertos o cerrados, etc.')
        materias["SEDM"] = Materia(id=33, fechacreacion=datetime.date.today(), abreviado='SEDM', nombre='Sist. Elect. Digital y Med.', descripcion='Así, una magnitud analógica es aquella que toma valores continuos. Una magnitud digital es aquella que toma un conjunto de valores discretos. La mayoría de las cosas que se pueden medir cuantitativamente aparecen en la naturaleza en forma analógica.')
        materias["TME"] = Materia(id=34, fechacreacion=datetime.date.today(), abreviado='TME', nombre='Tecnica Mater. Elect.', descripcion='No encontre una descripcion de esta materia: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla elementum enim non erat iaculis vestibulum. Curabitur malesuada eros quis urna cursus mollis. Cras sodales non neque ac ornare. Ut iaculis libero quis est interdum gravida. Aenean quis quam nisi. Donec maximus sagittis ligula eu suscipit. Nullam purus augue, dignissim a felis in.')
        materias["RRHH"] = Materia(id=35, fechacreacion=datetime.date.today(), abreviado='RRHH', nombre='Recursos Humanos', descripcion='El estudio de los recursos humanos: Dentro de una organización gestiona todas las actividades relacionadas con el personal que trabaja en ella. Los profesionales de los rrhh llevan a cabo la contratación, el despido, las vacaciones, remuneraciones y todas las áreas relacionadas.')
        
        cursos['1A'] = Curso(id=1, fechacreacion=datetime.date.today(), anio=anios['1'], division=divisiones['A'], especialidad = especialidades['VOID'])
        cursos['1B'] = Curso(id=2, fechacreacion=datetime.date.today(), anio=anios['1'], division=divisiones['B'], especialidad = especialidades['VOID'])
        cursos['1C'] = Curso(id=3, fechacreacion=datetime.date.today(), anio=anios['1'], division=divisiones['C'], especialidad = especialidades['VOID'])
        cursos['2A'] = Curso(id=4, fechacreacion=datetime.date.today(), anio=anios['2'], division=divisiones['A'], especialidad = especialidades['VOID'])
        cursos['2B'] = Curso(id=5, fechacreacion=datetime.date.today(), anio=anios['2'], division=divisiones['B'], especialidad = especialidades['VOID'])
        cursos['2C'] = Curso(id=6, fechacreacion=datetime.date.today(), anio=anios['2'], division=divisiones['C'], especialidad = especialidades['VOID'])
        cursos['3A'] = Curso(id=7, fechacreacion=datetime.date.today(), anio=anios['3'], division=divisiones['A'], especialidad = especialidades['VOID'])
        cursos['3B'] = Curso(id=8, fechacreacion=datetime.date.today(), anio=anios['3'], division=divisiones['B'], especialidad = especialidades['VOID'])
        cursos['3C'] = Curso(id=9, fechacreacion=datetime.date.today(), anio=anios['3'], division=divisiones['C'], especialidad = especialidades['VOID'])
        cursos['4A'] = Curso(id=10, fechacreacion=datetime.date.today(), anio=anios['4'], division=divisiones['A'], especialidad = especialidades['E'])
        cursos['4B'] = Curso(id=11, fechacreacion=datetime.date.today(), anio=anios['4'], division=divisiones['B'], especialidad = especialidades['EL'])
        cursos['4C'] = Curso(id=12, fechacreacion=datetime.date.today(), anio=anios['4'], division=divisiones['C'], especialidad = especialidades['P'])
        cursos['5A'] = Curso(id=13, fechacreacion=datetime.date.today(), anio=anios['5'], division=divisiones['A'], especialidad = especialidades['E'])
        cursos['5B'] = Curso(id=14, fechacreacion=datetime.date.today(), anio=anios['5'], division=divisiones['B'], especialidad = especialidades['EL'])
        cursos['5C'] = Curso(id=15, fechacreacion=datetime.date.today(), anio=anios['5'], division=divisiones['C'], especialidad = especialidades['P'])
        cursos['6A'] = Curso(id=16, fechacreacion=datetime.date.today(), anio=anios['6'], division=divisiones['A'], especialidad = especialidades['E'])
        cursos['6B'] = Curso(id=17, fechacreacion=datetime.date.today(), anio=anios['6'], division=divisiones['B'], especialidad = especialidades['EL'])
        cursos['6C'] = Curso(id=18, fechacreacion=datetime.date.today(), anio=anios['6'], division=divisiones['C'], especialidad = especialidades['P'])
        cursos['7A'] = Curso(id=19, fechacreacion=datetime.date.today(), anio=anios['7'], division=divisiones['A'], especialidad = especialidades['E'])
        cursos['7B'] = Curso(id=20, fechacreacion=datetime.date.today(), anio=anios['7'], division=divisiones['B'], especialidad = especialidades['EL'])
        cursos['7C'] = Curso(id=21, fechacreacion=datetime.date.today(), anio=anios['7'], division=divisiones['C'], especialidad = especialidades['P'])
        
        cronogramas['1A'] = Cronograma(id=1, fechacreacion=datetime.date.today(), curso = cursos['1A'])
        cronogramas['1B'] = Cronograma(id=2, fechacreacion=datetime.date.today(), curso = cursos['1B'])
        cronogramas['1C'] = Cronograma(id=3, fechacreacion=datetime.date.today(), curso = cursos['1C'])
        cronogramas['2A'] = Cronograma(id=4, fechacreacion=datetime.date.today(), curso = cursos['2A'])
        cronogramas['2B'] = Cronograma(id=5, fechacreacion=datetime.date.today(), curso = cursos['2B'])
        cronogramas['2C'] = Cronograma(id=6, fechacreacion=datetime.date.today(), curso = cursos['2C'])
        cronogramas['3A'] = Cronograma(id=7, fechacreacion=datetime.date.today(), curso = cursos['3A'])
        cronogramas['3B'] = Cronograma(id=8, fechacreacion=datetime.date.today(), curso = cursos['3B'])
        cronogramas['3C'] = Cronograma(id=9, fechacreacion=datetime.date.today(), curso = cursos['3C'])
        cronogramas['4A'] = Cronograma(id=10, fechacreacion=datetime.date.today(), curso = cursos['4A'])
        cronogramas['4B'] = Cronograma(id=11, fechacreacion=datetime.date.today(), curso = cursos['4B'])
        cronogramas['4C'] = Cronograma(id=12, fechacreacion=datetime.date.today(), curso = cursos['4C'])
        cronogramas['5A'] = Cronograma(id=13, fechacreacion=datetime.date.today(), curso = cursos['5A'])
        cronogramas['5B'] = Cronograma(id=14, fechacreacion=datetime.date.today(), curso = cursos['5B'])
        cronogramas['5C'] = Cronograma(id=15, fechacreacion=datetime.date.today(), curso = cursos['5C'])
        cronogramas['6A'] = Cronograma(id=16, fechacreacion=datetime.date.today(), curso = cursos['6A'])
        cronogramas['6B'] = Cronograma(id=17, fechacreacion=datetime.date.today(), curso = cursos['6B'])
        cronogramas['6C'] = Cronograma(id=18, fechacreacion=datetime.date.today(), curso = cursos['6C'])
        cronogramas['7A'] = Cronograma(id=19, fechacreacion=datetime.date.today(), curso = cursos['7A'])
        cronogramas['7B'] = Cronograma(id=20, fechacreacion=datetime.date.today(), curso = cursos['7B'])
        cronogramas['7C'] = Cronograma(id=21, fechacreacion=datetime.date.today(), curso = cursos['7C'])
        
        """ intente optimizarlo no salio como se esperaba unu
        cont = 0
        for i in cursos:
            for x in diasSemanas:
                cont += 1
                cronogramasDias[f'{cursos[i].anio}{cursos[i].division}'] = CronogramaDia(id=cont, fechacreacion=datetime.date.today(), cronograma = cronogramas[f'{cursos[i].anio}{cursos[i].division}'], dia = diasSemanas[x])        
        """
        cronogramasDias['1A Lunes'] = CronogramaDia(id=1, fechacreacion=datetime.date.today(), cronograma = cronogramas['1A'], dia = diasSemanas['1'])
        cronogramasDias['1A Martes'] = CronogramaDia(id=2, fechacreacion=datetime.date.today(), cronograma = cronogramas['1A'], dia = diasSemanas['2'])
        cronogramasDias['1A Miercoles'] = CronogramaDia(id=3, fechacreacion=datetime.date.today(), cronograma = cronogramas['1A'], dia = diasSemanas['3'])
        cronogramasDias['1A Jueves'] = CronogramaDia(id=4, fechacreacion=datetime.date.today(), cronograma = cronogramas['1A'], dia = diasSemanas['4'])
        cronogramasDias['1A Viernes'] = CronogramaDia(id=5, fechacreacion=datetime.date.today(), cronograma = cronogramas['1A'], dia = diasSemanas['5'])
        cronogramasDias['1B Lunes'] = CronogramaDia(id=6, fechacreacion=datetime.date.today(), cronograma = cronogramas['1B'], dia = diasSemanas['1'])
        cronogramasDias['1B Martes'] = CronogramaDia(id=7, fechacreacion=datetime.date.today(), cronograma = cronogramas['1B'], dia = diasSemanas['2'])
        cronogramasDias['1B Miercoles'] = CronogramaDia(id=8, fechacreacion=datetime.date.today(), cronograma = cronogramas['1B'], dia = diasSemanas['3'])
        cronogramasDias['1B Jueves'] = CronogramaDia(id=9, fechacreacion=datetime.date.today(), cronograma = cronogramas['1B'], dia = diasSemanas['4'])
        cronogramasDias['1B Viernes'] = CronogramaDia(id=10, fechacreacion=datetime.date.today(), cronograma = cronogramas['1B'], dia = diasSemanas['5'])
        cronogramasDias['1C Lunes'] = CronogramaDia(id=11, fechacreacion=datetime.date.today(), cronograma = cronogramas['1C'], dia = diasSemanas['1'])
        cronogramasDias['1C Martes'] = CronogramaDia(id=12, fechacreacion=datetime.date.today(), cronograma = cronogramas['1C'], dia = diasSemanas['2'])
        cronogramasDias['1C Miercoles'] = CronogramaDia(id=13, fechacreacion=datetime.date.today(), cronograma = cronogramas['1C'], dia = diasSemanas['3'])
        cronogramasDias['1C Jueves'] = CronogramaDia(id=14, fechacreacion=datetime.date.today(), cronograma = cronogramas['1C'], dia = diasSemanas['4'])
        cronogramasDias['1C Viernes'] = CronogramaDia(id=15, fechacreacion=datetime.date.today(), cronograma = cronogramas['1C'], dia = diasSemanas['5'])
        cronogramasDias['2A Lunes'] = CronogramaDia(id=16, fechacreacion=datetime.date.today(), cronograma = cronogramas['2A'], dia = diasSemanas['1'])
        cronogramasDias['2A Martes'] = CronogramaDia(id=17, fechacreacion=datetime.date.today(), cronograma = cronogramas['2A'], dia = diasSemanas['2'])
        cronogramasDias['2A Miercoles'] = CronogramaDia(id=18, fechacreacion=datetime.date.today(), cronograma = cronogramas['2A'], dia = diasSemanas['3'])
        cronogramasDias['2A Jueves'] = CronogramaDia(id=19, fechacreacion=datetime.date.today(), cronograma = cronogramas['2A'], dia = diasSemanas['4'])
        cronogramasDias['2A Viernes'] = CronogramaDia(id=20, fechacreacion=datetime.date.today(), cronograma = cronogramas['2A'], dia = diasSemanas['5'])
        cronogramasDias['2B Lunes'] = CronogramaDia(id=21, fechacreacion=datetime.date.today(), cronograma = cronogramas['2B'], dia = diasSemanas['1'])
        cronogramasDias['2B Martes'] = CronogramaDia(id=22, fechacreacion=datetime.date.today(), cronograma = cronogramas['2B'], dia = diasSemanas['2'])
        cronogramasDias['2B Miercoles'] = CronogramaDia(id=23, fechacreacion=datetime.date.today(), cronograma = cronogramas['2B'], dia = diasSemanas['3'])
        cronogramasDias['2B Jueves'] = CronogramaDia(id=24, fechacreacion=datetime.date.today(), cronograma = cronogramas['2B'], dia = diasSemanas['4'])
        cronogramasDias['2B Viernes'] = CronogramaDia(id=25, fechacreacion=datetime.date.today(), cronograma = cronogramas['2B'], dia = diasSemanas['5'])
        cronogramasDias['2C Lunes'] = CronogramaDia(id=26, fechacreacion=datetime.date.today(), cronograma = cronogramas['2C'], dia = diasSemanas['1'])
        cronogramasDias['2C Martes'] = CronogramaDia(id=27, fechacreacion=datetime.date.today(), cronograma = cronogramas['2C'], dia = diasSemanas['2'])
        cronogramasDias['2C Miercoles'] = CronogramaDia(id=28, fechacreacion=datetime.date.today(), cronograma = cronogramas['2C'], dia = diasSemanas['3'])
        cronogramasDias['2C Jueves'] = CronogramaDia(id=29, fechacreacion=datetime.date.today(), cronograma = cronogramas['2C'], dia = diasSemanas['4'])
        cronogramasDias['2C Viernes'] = CronogramaDia(id=30, fechacreacion=datetime.date.today(), cronograma = cronogramas['2C'], dia = diasSemanas['5'])
        cronogramasDias['3A Lunes'] = CronogramaDia(id=31, fechacreacion=datetime.date.today(), cronograma = cronogramas['3A'], dia = diasSemanas['1'])
        cronogramasDias['3A Martes'] = CronogramaDia(id=32, fechacreacion=datetime.date.today(), cronograma = cronogramas['3A'], dia = diasSemanas['2'])
        cronogramasDias['3A Miercoles'] = CronogramaDia(id=33, fechacreacion=datetime.date.today(), cronograma = cronogramas['3A'], dia = diasSemanas['3'])
        cronogramasDias['3A Jueves'] = CronogramaDia(id=34, fechacreacion=datetime.date.today(), cronograma = cronogramas['3A'], dia = diasSemanas['4'])
        cronogramasDias['3A Viernes'] = CronogramaDia(id=35, fechacreacion=datetime.date.today(), cronograma = cronogramas['3A'], dia = diasSemanas['5'])
        cronogramasDias['3B Lunes'] = CronogramaDia(id=36, fechacreacion=datetime.date.today(), cronograma = cronogramas['3B'], dia = diasSemanas['1'])
        cronogramasDias['3B Martes'] = CronogramaDia(id=37, fechacreacion=datetime.date.today(), cronograma = cronogramas['3B'], dia = diasSemanas['2'])
        cronogramasDias['3B Miercoles'] = CronogramaDia(id=38, fechacreacion=datetime.date.today(), cronograma = cronogramas['3B'], dia = diasSemanas['3'])
        cronogramasDias['3B Jueves'] = CronogramaDia(id=39, fechacreacion=datetime.date.today(), cronograma = cronogramas['3B'], dia = diasSemanas['4'])
        cronogramasDias['3B Viernes'] = CronogramaDia(id=40, fechacreacion=datetime.date.today(), cronograma = cronogramas['3B'], dia = diasSemanas['5'])
        cronogramasDias['3C Lunes'] = CronogramaDia(id=41, fechacreacion=datetime.date.today(), cronograma = cronogramas['3C'], dia = diasSemanas['1'])
        cronogramasDias['3C Martes'] = CronogramaDia(id=42, fechacreacion=datetime.date.today(), cronograma = cronogramas['3C'], dia = diasSemanas['2'])
        cronogramasDias['3C Miercoles'] = CronogramaDia(id=43, fechacreacion=datetime.date.today(), cronograma = cronogramas['3C'], dia = diasSemanas['3'])
        cronogramasDias['3C Jueves'] = CronogramaDia(id=44, fechacreacion=datetime.date.today(), cronograma = cronogramas['3C'], dia = diasSemanas['4'])
        cronogramasDias['3C Viernes'] = CronogramaDia(id=45, fechacreacion=datetime.date.today(), cronograma = cronogramas['3C'], dia = diasSemanas['5'])
        cronogramasDias['4A Lunes'] = CronogramaDia(id=46, fechacreacion=datetime.date.today(), cronograma = cronogramas['4A'], dia = diasSemanas['1'])
        cronogramasDias['4A Martes'] = CronogramaDia(id=47, fechacreacion=datetime.date.today(), cronograma = cronogramas['4A'], dia = diasSemanas['2'])
        cronogramasDias['4A Miercoles'] = CronogramaDia(id=48, fechacreacion=datetime.date.today(), cronograma = cronogramas['4A'], dia = diasSemanas['3'])
        cronogramasDias['4A Jueves'] = CronogramaDia(id=49, fechacreacion=datetime.date.today(), cronograma = cronogramas['4A'], dia = diasSemanas['4'])
        cronogramasDias['4A Viernes'] = CronogramaDia(id=50, fechacreacion=datetime.date.today(), cronograma = cronogramas['4A'], dia = diasSemanas['5'])
        cronogramasDias['4B Lunes'] = CronogramaDia(id=51, fechacreacion=datetime.date.today(), cronograma = cronogramas['4B'], dia = diasSemanas['1'])
        cronogramasDias['4B Martes'] = CronogramaDia(id=52, fechacreacion=datetime.date.today(), cronograma = cronogramas['4B'], dia = diasSemanas['2'])
        cronogramasDias['4B Miercoles'] = CronogramaDia(id=53, fechacreacion=datetime.date.today(), cronograma = cronogramas['4B'], dia = diasSemanas['3'])
        cronogramasDias['4B Jueves'] = CronogramaDia(id=54, fechacreacion=datetime.date.today(), cronograma = cronogramas['4B'], dia = diasSemanas['4'])
        cronogramasDias['4B Viernes'] = CronogramaDia(id=55, fechacreacion=datetime.date.today(), cronograma = cronogramas['4B'], dia = diasSemanas['5'])
        cronogramasDias['4C Lunes'] = CronogramaDia(id=56, fechacreacion=datetime.date.today(), cronograma = cronogramas['4C'], dia = diasSemanas['1'])
        cronogramasDias['4C Martes'] = CronogramaDia(id=57, fechacreacion=datetime.date.today(), cronograma = cronogramas['4C'], dia = diasSemanas['2'])
        cronogramasDias['4C Miercoles'] = CronogramaDia(id=58, fechacreacion=datetime.date.today(), cronograma = cronogramas['4C'], dia = diasSemanas['3'])
        cronogramasDias['4C Jueves'] = CronogramaDia(id=59, fechacreacion=datetime.date.today(), cronograma = cronogramas['4C'], dia = diasSemanas['4'])
        cronogramasDias['4C Viernes'] = CronogramaDia(id=60, fechacreacion=datetime.date.today(), cronograma = cronogramas['4C'], dia = diasSemanas['5'])
        cronogramasDias['5A Lunes'] = CronogramaDia(id=61, fechacreacion=datetime.date.today(), cronograma = cronogramas['5A'], dia = diasSemanas['1'])
        cronogramasDias['5A Martes'] = CronogramaDia(id=62, fechacreacion=datetime.date.today(), cronograma = cronogramas['5A'], dia = diasSemanas['2'])
        cronogramasDias['5A Miercoles'] = CronogramaDia(id=63, fechacreacion=datetime.date.today(), cronograma = cronogramas['5A'], dia = diasSemanas['3'])
        cronogramasDias['5A Jueves'] = CronogramaDia(id=64, fechacreacion=datetime.date.today(), cronograma = cronogramas['5A'], dia = diasSemanas['4'])
        cronogramasDias['5A Viernes'] = CronogramaDia(id=65, fechacreacion=datetime.date.today(), cronograma = cronogramas['5A'], dia = diasSemanas['5'])
        cronogramasDias['5B Lunes'] = CronogramaDia(id=66, fechacreacion=datetime.date.today(), cronograma = cronogramas['5B'], dia = diasSemanas['1'])
        cronogramasDias['5B Martes'] = CronogramaDia(id=67, fechacreacion=datetime.date.today(), cronograma = cronogramas['5B'], dia = diasSemanas['2'])
        cronogramasDias['5B Miercoles'] = CronogramaDia(id=68, fechacreacion=datetime.date.today(), cronograma = cronogramas['5B'], dia = diasSemanas['3'])
        cronogramasDias['5B Jueves'] = CronogramaDia(id=69, fechacreacion=datetime.date.today(), cronograma = cronogramas['5B'], dia = diasSemanas['4'])
        cronogramasDias['5B Viernes'] = CronogramaDia(id=70, fechacreacion=datetime.date.today(), cronograma = cronogramas['5B'], dia = diasSemanas['5'])
        cronogramasDias['5C Lunes'] = CronogramaDia(id=71, fechacreacion=datetime.date.today(), cronograma = cronogramas['5C'], dia = diasSemanas['1'])
        cronogramasDias['5C Martes'] = CronogramaDia(id=72, fechacreacion=datetime.date.today(), cronograma = cronogramas['5C'], dia = diasSemanas['2'])
        cronogramasDias['5C Miercoles'] = CronogramaDia(id=73, fechacreacion=datetime.date.today(), cronograma = cronogramas['5C'], dia = diasSemanas['3'])
        cronogramasDias['5C Jueves'] = CronogramaDia(id=74, fechacreacion=datetime.date.today(), cronograma = cronogramas['5C'], dia = diasSemanas['4'])
        cronogramasDias['5C Viernes'] = CronogramaDia(id=75, fechacreacion=datetime.date.today(), cronograma = cronogramas['5C'], dia = diasSemanas['5'])
        cronogramasDias['6A Lunes'] = CronogramaDia(id=76, fechacreacion=datetime.date.today(), cronograma = cronogramas['6A'], dia = diasSemanas['1'])
        cronogramasDias['6A Martes'] = CronogramaDia(id=77, fechacreacion=datetime.date.today(), cronograma = cronogramas['6A'], dia = diasSemanas['2'])
        cronogramasDias['6A Miercoles'] = CronogramaDia(id=78, fechacreacion=datetime.date.today(), cronograma = cronogramas['6A'], dia = diasSemanas['3'])
        cronogramasDias['6A Jueves'] = CronogramaDia(id=79, fechacreacion=datetime.date.today(), cronograma = cronogramas['6A'], dia = diasSemanas['4'])
        cronogramasDias['6A Viernes'] = CronogramaDia(id=80, fechacreacion=datetime.date.today(), cronograma = cronogramas['6A'], dia = diasSemanas['5'])
        cronogramasDias['6B Lunes'] = CronogramaDia(id=81, fechacreacion=datetime.date.today(), cronograma = cronogramas['6B'], dia = diasSemanas['1'])
        cronogramasDias['6B Martes'] = CronogramaDia(id=82, fechacreacion=datetime.date.today(), cronograma = cronogramas['6B'], dia = diasSemanas['2'])
        cronogramasDias['6B Miercoles'] = CronogramaDia(id=83, fechacreacion=datetime.date.today(), cronograma = cronogramas['6B'], dia = diasSemanas['3'])
        cronogramasDias['6B Jueves'] = CronogramaDia(id=84, fechacreacion=datetime.date.today(), cronograma = cronogramas['6B'], dia = diasSemanas['4'])
        cronogramasDias['6B Viernes'] = CronogramaDia(id=85, fechacreacion=datetime.date.today(), cronograma = cronogramas['6B'], dia = diasSemanas['5'])
        cronogramasDias['6C Lunes'] = CronogramaDia(id=86, fechacreacion=datetime.date.today(), cronograma = cronogramas['6C'], dia = diasSemanas['1'])
        cronogramasDias['6C Martes'] = CronogramaDia(id=87, fechacreacion=datetime.date.today(), cronograma = cronogramas['6C'], dia = diasSemanas['2'])
        cronogramasDias['6C Miercoles'] = CronogramaDia(id=88, fechacreacion=datetime.date.today(), cronograma = cronogramas['6C'], dia = diasSemanas['3'])
        cronogramasDias['6C Jueves'] = CronogramaDia(id=89, fechacreacion=datetime.date.today(), cronograma = cronogramas['6C'], dia = diasSemanas['4'])
        cronogramasDias['6C Viernes'] = CronogramaDia(id=90, fechacreacion=datetime.date.today(), cronograma = cronogramas['6C'], dia = diasSemanas['5'])
        cronogramasDias['7A Lunes'] = CronogramaDia(id=91, fechacreacion=datetime.date.today(), cronograma = cronogramas['7A'], dia = diasSemanas['1'])
        cronogramasDias['7A Martes'] = CronogramaDia(id=92, fechacreacion=datetime.date.today(), cronograma = cronogramas['7A'], dia = diasSemanas['2'])
        cronogramasDias['7A Miercoles'] = CronogramaDia(id=93, fechacreacion=datetime.date.today(), cronograma = cronogramas['7A'], dia = diasSemanas['3'])
        cronogramasDias['7A Jueves'] = CronogramaDia(id=94, fechacreacion=datetime.date.today(), cronograma = cronogramas['7A'], dia = diasSemanas['4'])
        cronogramasDias['7A Viernes'] = CronogramaDia(id=95, fechacreacion=datetime.date.today(), cronograma = cronogramas['7A'], dia = diasSemanas['5'])
        cronogramasDias['7B Lunes'] = CronogramaDia(id=96, fechacreacion=datetime.date.today(), cronograma = cronogramas['7B'], dia = diasSemanas['1'])
        cronogramasDias['7B Martes'] = CronogramaDia(id=97, fechacreacion=datetime.date.today(), cronograma = cronogramas['7B'], dia = diasSemanas['2'])
        cronogramasDias['7B Miercoles'] = CronogramaDia(id=98, fechacreacion=datetime.date.today(), cronograma = cronogramas['7B'], dia = diasSemanas['3'])
        cronogramasDias['7B Jueves'] = CronogramaDia(id=99, fechacreacion=datetime.date.today(), cronograma = cronogramas['7B'], dia = diasSemanas['4'])
        cronogramasDias['7B Viernes'] = CronogramaDia(id=100, fechacreacion=datetime.date.today(), cronograma = cronogramas['7B'], dia = diasSemanas['5'])
        cronogramasDias['7C Lunes'] = CronogramaDia(id=101, fechacreacion=datetime.date.today(), cronograma = cronogramas['7C'], dia = diasSemanas['1'])
        cronogramasDias['7C Martes'] = CronogramaDia(id=102, fechacreacion=datetime.date.today(), cronograma = cronogramas['7C'], dia = diasSemanas['2'])
        cronogramasDias['7C Miercoles'] = CronogramaDia(id=103, fechacreacion=datetime.date.today(), cronograma = cronogramas['7C'], dia = diasSemanas['3'])
        cronogramasDias['7C Jueves'] = CronogramaDia(id=104, fechacreacion=datetime.date.today(), cronograma = cronogramas['7C'], dia = diasSemanas['4'])
        cronogramasDias['7C Viernes'] = CronogramaDia(id=105, fechacreacion=datetime.date.today(), cronograma = cronogramas['7C'], dia = diasSemanas['5'])
        
        for x in anios:
            anios[x].save()

        for x in divisiones:
            divisiones[x].save()

        for x in especialidades:
            especialidades[x].save()
        
        for x in diasSemanas:
            diasSemanas[x].save()

        for x in materias:
            materias[x].save()

        for x in contenidosMaterias:
            contenidosMaterias[x].save()

        for x in cursos:
            cursos[x].save()

        for x in cronogramas:
            cronogramas[x].save()
            
        for x in cronogramasDias:
            cronogramasDias[x].save()

        self.stdout.write(self.style.SUCCESS("this worked"))