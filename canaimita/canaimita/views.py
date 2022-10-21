from ast import parse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UsuarioForm, preguntas
from . import facultades, habla

#VARIABLES QUE SERAN ENVIADAS A LOS HTML 
global errorcito
errorcito = "a"
nombreUsuario = "JimmyBoy"
respuestasPreguntas = [0,0,0,0,0,0]
prediccion = "fracaso"
#---------------------------------------


def pagina1(request):
	return HttpResponse('Funciono')

def mainpage(request):
	if request.method == 'POST': 
		return redirect('/form/01/')
	return render(request, 'main.html')

def form1(request): 
	errorcito = ""
	if request.method == 'POST':
		if request.POST["nombre"].isalpha():
			print("el request es",request.POST)
			global nombreUsuario
			nombreUsuario = request.POST["nombre"]
			print(nombreUsuario)
			form = UsuarioForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/form/02/')
		else:
			errorcito = "Ha introducido un nombre invalido"
			form = UsuarioForm()
	else:
		form = UsuarioForm()
		habla.habla('Hola. ¡Soy Chamabot! ¿Podrías decirme tu nombre?')
	
	return render(request, 'form1.html', {'form' : form, 'errorcito' : errorcito})

def form2(request):
	if request.method == 'POST': 
		global respuestasPreguntas
		global prediccion
		
		for i in range (0,6):
			preguntoski = "pregunta" + str(i+1)
			respuestasPreguntas[i] = request.POST[preguntoski]	

		print(respuestasPreguntas) 
		prediccion = facultades.RealizarPrediccion(respuestasPreguntas)
		return redirect('/prediccion/')
	else:
		form = preguntas()
		habla.habla('Hola' + nombreUsuario + ',me encantaría saber más de ti… Por favor ayúdame a conocerte mejor, respondiendo las siguientes preguntas')
	return render(request, 'form2.html', {'form' : form, 'nombreUsuario': nombreUsuario})

def form3(request): 
	return render(request, 'pagina3.html')

def prediccion(request):
	habla.habla(nombreUsuario + "," + prediccion)
	return render(request, 'prediccion.html', {'prediccion' : prediccion, 'nombreUsuario': nombreUsuario +"," })