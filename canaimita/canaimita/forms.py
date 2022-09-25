from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import Usuario

OPCIONES_1=[
    ('1','Matemática, Física y Química'),
    ('2','Ciencias Sociales, Lenguaje y Comunicacion'),
    ('3','Computacion'),
    ('4','Artes Plasticas o Dibujo Tecnico'),
]
OPCIONES_2=[
    ('1','Leyendo'),
    ('2','Armando y Desarmando cosas'),
    ('3','Dibujando o Tomando Fotografías'),
    ('4','Escribiendo programas o juegos en la computadora'),
]
OPCIONES_3=[
    ('1','Usando Fórmulas Matemáticas'),
    ('2','Hablando con Personas'),
    ('3','Empleando el Arte y la cultura'),
    ('4','Empleando la Tecnología'),
]
OPCIONES_4=[
    ('1','Pensamiento Estratégico'),
    ('2','Gran Creatividad'),
    ('3','Manejo de Tiempo'),
    ('4','Capacidad de Negociacion'),
    ('5','Gran Comprension del Color, la forma y la figura'),
]
OPCIONES_5=[
    ('1','El desarrollo de la solución mediante la aplicación de procedimientos prácticos y matemáticos'),
    ('2','Reflexionas sobre las actitudes y comportamientos que llevaron a esas situaciones y tomas una actitud crítica sobre lo que va ocurriendo'),
    ('3','Identificas y analizas el problema para luego identificar los criterios de decisión y ponderarlos'),
    ('4','Buscas negociar con el causante del problema analizando la causa para así pasar o tomar decisiones implementando un plan de acción'),
    ('5','Buscas estructurar un mensaje de forma coherente y creativa para aclarar la situación'),
]
OPCIONES_6=[
    ('1','En un departamento de calidad'),
    ('2','Creando contenido corporativo gestionado las redes sociales de una empresa'),
    ('3','En una empresa llevando el análisis de mercadeo'),
    ('4','En una empresa privada consultando y atendiendo todos los procesos jurídicos y corporativos'),
    ('5','En una agencia de publicidad creando revistas flyers entre otros elementos.'),
]
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class preguntas(forms.Form):
    pregunta1 = forms.CharField(label ='1. ¿Cuál grupo de las siguientes materias te gustaba más estudiar en bachillerato?',widget=forms.Select(choices=OPCIONES_1))
    pregunta2 = forms.CharField(label ='2. ¿Cuál sería tu forma favorita de pasar el tiempo?',widget=forms.Select(choices=OPCIONES_2))
    pregunta3 = forms.CharField(label ='3. ¿Cual seria tu herramienta favorita para resolver un problema?',widget=forms.Select(choices=OPCIONES_3))
    pregunta4 = forms.CharField(label ='4. Te consideras más una persona con:',widget=forms.Select(choices=OPCIONES_4))
    pregunta5 = forms.CharField(label ='5. Al resolver un problema te enfocas más en:',widget=forms.Select(choices=OPCIONES_5))
    pregunta6 = forms.CharField(label ='6. Te gustaría trabajar más en:',widget=forms.Select(choices=OPCIONES_6))