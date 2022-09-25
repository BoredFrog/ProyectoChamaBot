from ast import parse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import prueba, prueba2
from .forms import UsuarioForm, preguntas

#VARIABLE NOMBRE USUARIO y OPCIONES 
nombreUsuario = "JimmyBoy"
respuestasPreguntas = [0,0,0,0,0,0]

def pagina2(request): 
	result  = prueba.JimmyStavisky() #PRIMERA SOLUCION: LLAMAR A UNA FUNCION APENAS INICIA LA VIEW, Y DEVOLVER EL RESULTADO AL TEMPLATE
	return render(request, 'pagina2.html', {'resulton': result})

def pagina3(request): 
	#PRUEBA 2: LLAMAR METODO DIRECTAMENTE DEL HTML - FUNCIONA
	return render(request, 'pagina3.html', {'jimmy2': prueba2})

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
		print("el request es:", request.POST)
		
		for i in range (0,6):
			preguntoski = "pregunta" + str(i+1)
			respuestasPreguntas[i] = request.POST[preguntoski]		
		print(respuestasPreguntas) #Soy un webo

		return redirect('/form/03/')
	else:
		form = preguntas()
	return render(request, 'form2.html', {'form' : form, 'nombreUsuario': nombreUsuario})

def form3(request): 
	return render(request, 'pagina3.html', {'jimmy2': prueba2})