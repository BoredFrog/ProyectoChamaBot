from ast import parse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UsuarioForm, preguntas
from . import facultades

#VARIABLES QUE SERAN ENVIADAS A LOS HTML 
nombreUsuario = "JimmyBoy"
respuestasPreguntas = [0,0,0,0,0,0]
prediccion = "fracaso"
#---------------------------------------


def pagina1(request):
	return HttpResponse('Funciono')

def form1(request): 
	if request.method == 'POST':
		print("el request es",request.POST)
		global nombreUsuario
		nombreUsuario = request.POST["nombre"]
		print(nombreUsuario)
		form = UsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/form/02/')
	else:
		form = UsuarioForm()
	
	return render(request, 'form1.html', {'form' : form})

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
	return render(request, 'form2.html', {'form' : form, 'nombreUsuario': nombreUsuario})

def form3(request): 
	return render(request, 'pagina3.html')

def prediccion(request):
	return render(request, 'prediccion.html', {'prediccion' : prediccion })