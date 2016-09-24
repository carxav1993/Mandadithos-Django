#encoding:utf-8
from django.shortcuts import render, redirect
from .models import Empresa, Telefono, Servicio, Objetivo, Ventaja_Competitiva, Suscripcion, Contacto, Trabajo, Locales, ImagenesPublicidad
from django.http import JsonResponse, HttpResponse
from .forms import TrabajoForm, LocalesForm

# Create your views here.
def inicio(request):
	empresa = Empresa.objects.get(id=1)
	telefonos = Telefono.objects.all()
	imagenes = ImagenesPublicidad.objects.all()[:4]
	return render(request, 'empresa/index.html', {'empresa':empresa, 'telefonos':telefonos,'imagenes':imagenes})

def empresa(request):
	empresa = Empresa.objects.get(id=1)
	ventaja1 = Ventaja_Competitiva.objects.get(id=1)
	ventaja2 = Ventaja_Competitiva.objects.get(id=2)
	ventaja3 = Ventaja_Competitiva.objects.get(id=3)
	ventaja4 = Ventaja_Competitiva.objects.get(id=4)
	objetivos = Objetivo.objects.all()
	return render(request, 'empresa/empresa.html',{'empresa':empresa, 'objetivos':objetivos, 'ventaja1':ventaja1, 'ventaja2':ventaja2, 'ventaja3':ventaja3, 'ventaja4':ventaja4})

def servicios(request):
	empresa = Empresa.objects.get(id=1)
	servicios = Servicio.objects.all()
	return render(request, 'empresa/servicios.html', {'servicios':servicios, 'empresa':empresa})

def contactenos(request):
	empresa = Empresa.objects.get(id=1)
	telefonos = Telefono.objects.all()
	return render(request, 'empresa/contactenos.html', {'empresa':empresa, 'telefonos':telefonos})

def registrate(request):

	if request.method == "POST":
		print 'entro al post'
		if 'trabajo_form' in request.POST:
			trabForm = TrabajoForm(request.POST)
			print 'llego a trabajo_form'
			if trabForm.is_valid():
				print "Formulario Válido"
				empresa = Empresa.objects.get(id=1)
				modelForm = TrabajoForm()
				localForm = LocalesForm()
				return render("empresa/registrate",{'empresa':empresa})
		
		if 'locales_form' in request.POST:
			localForm = LocalesForm(request.POST)
			if localForm.is_valid():
				print "formulario valido"
				return render("empresa/registrate")
	else:
		modelForm = TrabajoForm()
		empresa = Empresa.objects.get(id=1)
		localForm = LocalesForm()
	return render(request, 'empresa/registrate.html', {'empresa':empresa,'trabajo':modelForm, 'locales':localForm})

#suscribir el coreo por ajax
def registro_ajax(request):
	if request.is_ajax():
		correo =  request.GET['correo']
		fecha = request.GET['fecha']
		print correo + fecha
		print Suscripcion.objects.filter(email=correo)
		print Suscripcion.objects.filter(email=correo).count()
		suscripciones = Suscripcion.objects.filter(email=correo).count()		
		if suscripciones>0:
			response = JsonResponse({'respuesta':'no'})
			return HttpResponse(response.content)
		else:
			sus = Suscripcion()
			sus.email = correo
			sus.fecha = fecha
			sus.save()
			response = JsonResponse({'correo':correo, 'respuesta':'si'})
			return HttpResponse(response.content)
	else:
		return redirect('/')

def ajax_contacto(request):
	if request.is_ajax():
		nombre = request.GET['nombre']
		email = request.GET['correo']
		asunto = request.GET['asunto']
		mensaje = request.GET['mensaje']
		fecha = request.GET['fecha']
		print nombre + email + asunto + mensaje + fecha
		contact = Contacto()
		contact.nombres_apellidos = nombre
		contact.email = email
		contact.asunto = asunto
		contact.mensaje = mensaje
		contact.fecha = fecha
		contact.leido = False
		contact.save()
		response = JsonResponse({'respuesta':'si'})
		return HttpResponse(response.content)
	else:
		return redirect('/')	

def trabajo_ajax(request):
	if request.is_ajax:
		trab = Trabajo()
		trab.nombres = request.GET['nombres']
		trab.apellido_paterno = request.GET['apellido1']
		trab.apellido_materno = request.GET['apellido2']
		trab.fecha_nacimiento = request.GET['nacimiento']
		trab.email = request.GET['email']
		trab.direccion = request.GET['direccion']
		trab.convencional = request.GET['convencional']
		trab.celular = request.GET['celular']
	 	trab.provincia = request.GET['provincia']
	 	trab.ciudad = request.GET['ciudad']
	 	trab.estado_civil = request.GET['civil']
	 	trab.curriculum = request.GET['curriculum']
		trab.save()
		response = JsonResponse({'respuesta':'llego'})
		return HttpResponse(response.content)
	else:
		return redirect("/")

def locales_ajax(request):
	if request.is_ajax:
		print request.GET
		local = Locales()
		local.razon_social = request.GET['razon']
		local.provincia = request.GET['provincia']
		local.ciudad = request.GET['ciudad']
		local.direccion = request.GET['direccion']
		local.referencias = request.GET['referencias']
		local.email = request.GET['email']
		local.convencional1 = request.GET['convencional1']
		local.convencional2 = request.GET['convencional2']
		local.celular1 = request.GET['celular1']
		local.celular2 = request.GET['celular2']
		local.mensaje = request.GET['mensaje']
		local.save()
		response = JsonResponse({'respuesta':'llego'})
		return HttpResponse(response.content)
	else:
		return redirect("/")
		