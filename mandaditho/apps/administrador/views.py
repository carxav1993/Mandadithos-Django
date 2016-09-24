#encoding:utf-8
from django.shortcuts import render, redirect, get_object_or_404
from apps.empresa.models import Empresa, Telefono, Objetivo, Tipo_servicio, Servicio, Suscripcion, Contacto, Ventaja_Competitiva, Locales, Trabajo 
from .forms import LoginForm, EmpresaForm,TelefonoForm,ObjetivoForm,SuscripcionForm,ContactoForm,Ventaja_CompetitivaForm,LocalesForm,TrabajoForm,TipoServicioForm, ServicioForm, CorreoMasivoForm
from django.contrib.auth import authenticate, login as auth_login, logout
from apps.users.models import User
from django.core.mail import send_mail, EmailMessage
# Create your views here.
def login(request):
	mensaje = ""
	print request.POST
	if request.POST:
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			user = authenticate(username = login_form.cleaned_data['username'],	password = login_form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					print "Entro en el si es active"
					print user
					auth_login(request, user)
					return redirect('/administrador/inicio')
			else:
				mensaje = "El usuario o contraseña incorrectos."
				return render(request, 'administrador/login.html', {'login_form':login_form, 'mensaje':mensaje})
	else:
		login_form = LoginForm()
	return render(request, 'administrador/login.html', {'login_form':login_form, 'mensaje':mensaje})

def LogOut(request):
	logout(request)
	return redirect('/administrador/login')

def inicio(request):
	empresa = get_object_or_404(Empresa, pk=1)
	return render (request, 'administrador/inicio.html',{'empresa':empresa})

def empresa(request):
	empresa = get_object_or_404(Empresa, pk=1)
	if request.method == 'POST':
		empresa_form = EmpresaForm(request.POST, request.FILES, instance=empresa) 
		if empresa_form.is_valid():
			empresa_form.save()
			return render(request, 'administrador/empresa.html', {'empresa':empresa, 'empresa_form':empresa_form,'mensaje':'Cambios actualizados satisfactoriamente'})
		else:
			return render(request, 'administrador/empresa.html', {'empresa':empresa, 'empresa_form':empresa_form,'mensaje':'Existen errores, no se pudo actualizar.'})
	else:
		empresa_form = EmpresaForm(instance=empresa)
		return render(request, 'administrador/empresa.html', 
			{
			'empresa':empresa,'empresa_form':empresa_form,
			'mensaje':'Todos los campos que se encuentran presentes son requeridos (*), por lo que deben contener información.'
			 })

#Telefonos - Añadir Teléfono
def Anadir_Telefono(request):
	if request.method == 'POST':
		telf = TelefonoForm(request.POST)
		if telf.is_valid():
			telf.save()
			return redirect('/administrador/telefonos')
		else:
			return render(request, 'administrador/telefonos/anadir_telefono.html', {'telefono':telf})
	else:
		telf = TelefonoForm()
		return render(request, 'administrador/telefonos/anadir_telefono.html', {'telefono':telf})

#Telefonos - Listar Telefonos
def telefonos(request):
	telef = Telefono.objects.all()
	return render(request, 'administrador/telefonos/telefonos.html', {'telefonos':telef})

#Telefonos - Editar Telefonos
def Editar_Telefono(request, telefono_id):
	telf = get_object_or_404(Telefono, id=telefono_id)

	if request.method == 'POST':
		telefono_form = TelefonoForm(request.POST, instance=telf)
		if telefono_form.is_valid():
			telefono_form.save()
			return redirect('/administrador/telefonos')
		else:
			return render(request, 'administrador/telefonos/editar_telefono.html', {'telefono_form':telefono_form})
	else:
		telefono_form = TelefonoForm(instance=telf)
		return render(request, 'administrador/telefonos/editar_telefono.html', {'telefono_form':telefono_form})

#Telefonos - Eliminar Telefono
def Eliminar_Telefono(request, telefono_id):
	telf = get_object_or_404(Telefono, id=telefono_id)
	if request.method == 'POST':
		telf.delete()
		return redirect('/administrador/telefonos')
	else:
		return render(request, 'administrador/telefonos/eliminar_telefono.html', {'telefono':telf})

########################OBJETIVOS#####################
#Objetivos - crear
def Anadir_Objetivo(request):
	if request.method == 'POST':
		objetivo_form = ObjetivoForm(request.POST)
		if objetivo_form.is_valid():
			objetivo_form.save()
			return redirect('/administrador/objetivos')
		else:
			return render(request, 'administrador/objetivos/anadir_objetivo.html', {'objetivo_form':objetivo_form})	
	else:
		objetivo_form = ObjetivoForm()
		return render(request, 'administrador/objetivos/anadir_objetivo.html', {'objetivo_form':objetivo_form})

#Objetivos - listado
def Objetivos(request):
	objetivos = Objetivo.objects.all()
	return render(request, 'administrador/objetivos/objetivos.html', {'objetivos':objetivos})

#Objetivos - editar objetivo
def Editar_Objetivos(request, objetivo_id):
	obj = get_object_or_404(Objetivo, id=objetivo_id)
	if request.method == 'POST':
		objetivo = ObjetivoForm(request.POST, instance=obj)
		if objetivo.is_valid():
			objetivo.save()
			return redirect('/administrador/objetivos')
		else:
			return render(request, 'administrador/objetivos/editar_objetivo.html', {'objetivo':objetivo})
	else:
		objetivo = ObjetivoForm(instance=obj)
		return render(request, 'administrador/objetivos/editar_objetivo.html', {'objetivo':objetivo})

#Objetivos - eliminar objetivo
def Eliminar_Objetivo(request, objetivo_id):
	obj = get_object_or_404(Objetivo, id=objetivo_id)
	if(request.method == 'POST'):
		obj.delete()
		return redirect('/administrador/objetivos')
	else:
		return render(request, 'administrador/objetivos/eliminar_objetivo.html', {'objetivo':obj})

#########################################Suscripciones#####################################################
#Suscripciones - Listado
def Suscripciones(request):
	suscripciones = Suscripcion.objects.all().order_by('-fecha')
	return render(request, 'administrador/suscripciones/suscripciones.html', {'suscripciones':suscripciones})

#Suscripciones - Anadir Suscripción
def Anadir_Suscripcion(request):
	if request.method == 'POST':
		suscrip = SuscripcionForm(request.POST)
		if suscrip.is_valid():
			correo = suscrip.cleaned_data['email']
			numero = Suscripcion.objects.filter(email=correo).count()
			if numero > 0:
				return redirect('/administrador/suscripciones')
			else:
				suscrip.save()
				return redirect('/administrador/suscripciones')
		else:
			return render(request, 'administrador/suscripciones/anadir_email.html', {'suscripcion': suscrip})
	else:
		suscrip = SuscripcionForm()
		return render(request, 'administrador/suscripciones/anadir_email.html', {'suscripcion': suscrip})

#Suscripcion - Editar Suscripción
def Editar_Suscripcion(request, suscripcion_id):
	suscrip = get_object_or_404(Suscripcion, id=suscripcion_id)
	if request.method == 'POST':
		suscrip_form = SuscripcionForm(request.POST, instance=suscrip)
		if suscrip_form.is_valid():
			suscrip_form.save()
			return redirect('/administrador/suscripciones')
		else:
			return render(request, 'administrador/suscripciones/editar_suscripcion.html', {'suscripcion':suscrip_form})	
	else:
		suscrip_form = SuscripcionForm(instance=suscrip)
		return render(request, 'administrador/suscripciones/editar_suscripcion.html', {'suscripcion':suscrip_form})

#Suscripcion - Eliminar Suscripción
def Eliminar_Suscripcion(request, suscripcion_id):
	suscr = get_object_or_404(Suscripcion, id=suscripcion_id)
	if request.method == 'POST':
		suscr.delete()
		return redirect('/administrador/suscripciones')
	else:
		return render(request, 'administrador/suscripciones/eliminar_suscripcion.html', {'suscripcion':suscr})

############################Contáctenos

#Contactenos - listado de contáctenos
def Contactenos(request):
	contacts = Contacto.objects.all().order_by('-fecha')
	return render(request, 'administrador/contactenos/contactenos.html', {'contactenos':contacts})

#Contactenos - ver contáctenos
def Ver_Contactenos(request, contactenos_id):
	contact = get_object_or_404(Contacto, id=contactenos_id)
	if request.method == 'POST':
		contact_form = ContactoForm(request.POST, instance=contact)
		if contact_form.is_valid():
			contact_form.save()
			return redirect('/administrador/contactenos')
	else:
		contact_form = ContactoForm(instance=contact)
		print contact_form
		return render(request, 'administrador/contactenos/ver_contactenos.html', {'contacto':contact_form})

#Contáctenos - Eliminar contáctenos
def Eliminar_Contactenos(request, contactenos_id):
	suscr = get_object_or_404(Contacto, id=contactenos_id)
	if request.method == 'POST':
		suscr.delete()
		return redirect('/administrador/contactenos')
	else:
		return render(request, 'administrador/contactenos/eliminar_contactenos.html', {'contacto':suscr})

##################Venatajas competitivas
#Ventajas competitivas - Listado
def Ventajas_Competitivas(request):
	vent = Ventaja_Competitiva.objects.all()
	return render(request, 'administrador/ventajas_competitivas/ventajas_competitivas.html',{'ventajas':vent})

#Ventajas competitivas - anadir
def Anadir_Ventaja(request):
	if request.method == 'POST':
		vent = Ventaja_CompetitivaForm(request.POST)
		if vent.is_valid():
			vent.save()
			return redirect('/administrador/ventajas')
		else:
			return render(request,'administrador/ventajas_competitivas/anadir_ventaja.html',{'ventaja':vent})
	else:
		vent = Ventaja_CompetitivaForm()
		return render(request,'administrador/ventajas_competitivas/anadir_ventaja.html',{'ventaja':vent})

#Ventajas competitivas - editar
def Editar_Ventaja(request, ventaja_id):
	ventaja = get_object_or_404(Ventaja_Competitiva, id=ventaja_id)
	if request.method == 'POST':
		ventaja_form = Ventaja_CompetitivaForm(request.POST, instance=ventaja)
		if ventaja_form.is_valid():
			ventaja_form.save()
			return redirect('/administrador/ventajas')
		else:
			return render(request,'administrador/ventajas_competitivas/editar_ventaja.html',{'ventaja':ventaja_form})	
	else:
		ventaja_form = Ventaja_CompetitivaForm(instance=ventaja)
		return render(request,'administrador/ventajas_competitivas/editar_ventaja.html',{'ventaja':ventaja_form})

#Ventajas competitivas - eliminar
def Eliminar_Ventaja(request, ventaja_id):
	ventaja = get_object_or_404(Ventaja_Competitiva, id=ventaja_id)
	if request.method == 'POST':
		ventaja.delete()
		return redirect('/administrador/ventajas')
	else:
		return render (request, 'administrador/ventajas_competitivas/eliminar_ventaja.html', {'ventaja':ventaja})

#############LOCALES###############
#Locales - listar locales
def Lista_Locales(request):
	local = Locales.objects.all().order_by('-fecha_registro')
	return render(request, 'administrador/solicitudes/locales/locales.html',{'locales':local})

#Locales - Editar locales
def Editar_Local(request, local_id):
	local = get_object_or_404(Locales, id=local_id)
	if request.method == 'POST':
		local_form = LocalesForm(request.POST, instance=local)
		if local_form.is_valid():
			local_form.save()
			return redirect('/administrador/locales')
		else:
			return render(request, 'administrador/solicitudes/locales/editar_local.html',{'local':local_form})
	else:
		local_form = LocalesForm(instance=local)		
		return render(request, 'administrador/solicitudes/locales/editar_local.html',{'local':local_form})

#Locales - Eliminar local
def Eliminar_Local(request, local_id):
	local = get_object_or_404(Locales, id=local_id)
	if request.method == 'POST':
		local.delete()
		return redirect('/administrador/locales')
	else:
		return render(request,'administrador/solicitudes/locales/eliminar_local.html',{'local':local})

######################Trabajo##################
#Trabajos
def Trabajos(request):
	trabajos = Trabajo.objects.all().order_by('-fecha_solicitud')
	return render(request, 'administrador/solicitudes/trabajo/trabajos.html',{'trabajos':trabajos})

#Ver trabajo
def Ver_Trabajo(request, trabajo_id):
	trab = get_object_or_404(Trabajo, id=trabajo_id)
	if request.method == 'POST':
		trab_form = TrabajoForm(request.POST, instance=trab)
		if trab_form.is_valid():
			trab_form.save()
			return redirect('/administrador/trabajos')
		else:
			return render(request, 'administrador/solicitudes/trabajo/ver_trabajo.html',{'trabajo':trab_form})
	else:
		trab_form = TrabajoForm(instance=trab)
		return render(request, 'administrador/solicitudes/trabajo/ver_trabajo.html',{'trabajo':trab_form})

#Eliminar trabajo
def Eliminar_Trabajo(request, trabajo_id):
	trab = get_object_or_404(Trabajo, id=trabajo_id)
	if request.method == 'POST':
		trab.delete()
		return redirect('/administrador/trabajos')
	else:
		return render(request, 'administrador/solicitudes/trabajo/eliminar_trabajo.html',{'trabajo':trab})

################TIPOS SERVICIOS################
def Tipos_Servicios(request):
	tipos = Tipo_servicio.objects.all()
	return render(request, 'administrador/servicios/tipos/tipos.html',{'tipos':tipos})
 
def Anadir_Tipo(request):
	if request.method == 'POST':
 		tipo_form = TipoServicioForm(request.POST)
 		if tipo_form.is_valid():
 			tipo_form.save()
 			return redirect('/administrador/tiposServicios')
 		else:
 			return render(request, 'administrador/servicios/tipos/anadir_tipo.html',{'tipo':tipo_form})
 	else:
 		tipo_form = TipoServicioForm()
 		return render(request, 'administrador/servicios/tipos/anadir_tipo.html',{'tipo':tipo_form})

def Editar_Tipo(request, tipo_id):
 	tipo = get_object_or_404(Tipo_servicio, id=tipo_id)
 	if request.method == 'POST':
 		tipo_form = TipoServicioForm(request.POST, instance=tipo)
 		if tipo_form.is_valid():
 			tipo_form.save()
 			return redirect('/administrador/tiposServicios')
		else:
			return render(request, 'administrador/servicios/tipos/editar_tipo.html',{'tipo':tipo_form})
 	else:
 		tipo_form = TipoServicioForm(instance=tipo)
 		return render(request, 'administrador/servicios/tipos/editar_tipo.html',{'tipo':tipo_form})

def Eliminar_Tipo(request, tipo_id):
	tipo = get_object_or_404(Tipo_servicio, id=tipo_id)
	if request.method == 'POST':
		tipo.delete()
		return redirect('/administrador/tiposServicios')
	else:
		return render(request,'administrador/servicios/tipos/eliminar_tipo.html',{'tipo':tipo})
#########################SERVICIOS##############
#Servicios - listar servicios
def Servicios(request):
	servicios = Servicio.objects.all()
	return render(request,'administrador/servicios/servicios/servicios.html',{'servicios':servicios})

#Servicios - Anadir_Servicio
def Anadir_Servicio(request):
	if request.method == 'POST':
		servicio = ServicioForm(request.POST)
		if servicio.is_valid():
			servicio.save()
			return redirect('/administrador/servicios')
		else:
			return render(request, 'administrador/servicios/servicios/anadir_servicio.html',{'servicio':servicio})
	else:
		servicio = ServicioForm()
		return render(request, 'administrador/servicios/servicios/anadir_servicio.html',{'servicio':servicio})

#Servicios - Editar Servicio
def Editar_Servicio(request, servicio_id):
	serv = get_object_or_404(Servicio, id=servicio_id)
	if request.method == 'POST':
		servicio_form = ServicioForm(request.POST, request.FILES, instance=serv)
		if servicio_form.is_valid():
			servicio_form.save()
			return redirect('/administrador/servicios')
		else:
			return render(request,'administrador/servicios/servicios/editar_servicio.html',{'servicio':servicio_form,'ser':serv})
	else:
		servicio_form = ServicioForm(instance=serv)
		return render(request,'administrador/servicios/servicios/editar_servicio.html',{'servicio':servicio_form,'ser':serv})

#servicios - eliminar
def Eliminar_Servicio(request, servicio_id):
	serv = get_object_or_404(Servicio, id=servicio_id)
	if request.method == 'POST':
		serv.delete()
		return redirect('/administrador/servicios')
	else:
		return render(request,'administrador/servicios/servicios/eliminar_servicios.html',{'servicio':serv})

###########Correo Masivo###########
def Correo_Masivo(request):
	if request.method == 'POST':
		correo_form = CorreoMasivoForm(request.POST)
		if correo_form.is_valid():
			asunto = correo_form.cleaned_data['asunto']
			mensaje = correo_form.cleaned_data['mensaje']
			print asunto + mensaje
			#send_mail(asunto, mensaje, 'cvcarlosvega93@gmail.com', ['carlos_barce93@hotmail.com'], fail_silently=False)
			email = EmailMessage(asunto,mensaje,'cvcarlosvega93@gmail.com',to=['carlos_barce93@hotmail.com'])
			email.send()
    		return redirect('/administrador/suscripciones')
	else:
		correo_form = CorreoMasivoForm()
		return render(request, 'administrador/suscripciones/enviar_correo.html',{'correo':correo_form})