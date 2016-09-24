#encoding:utf-8
from django import forms
from apps.empresa.models import Empresa, Telefono, Objetivo, Suscripcion, Contacto, Ventaja_Competitiva, Locales, Trabajo, Tipo_servicio, Servicio

my_default_errors = {
    'required': 'Este campo es requerido',
    'invalid': 'Ingrese un valor válido',
}

#Este es para los objetivos
OBJ = ( ('LP','Largo Plazo'),('MP','Mediano Plazo'),('CP','Corto Plazo'),)

#Este es para los teléfonos
TYPE = (('CN','Convencional'),('CL','Celular'),)
OPER = (('CL','Claro'),('MO','Movistar'),('CNT','CNT'),('TW','Tuenti'),)

#Para los locales y trabajo
PROV = ( ('AZ','Azuay'),('BO','Bolivar'),('CA','Cañar'),('CR','Carchi'),('CH','Chimborazo'),('CO','Cotopaxi'),
 		('OR','El Oro'),('ES','Esmeraldas'),('GA','Galápagos'),('GU','Guayas'),('IM','Imbabura'),('LO','Loja'),
 		('LR','Los Rios'),('MA','Manabi'),('MS','Morona Santiago'),('NA','Napo'),('OR','Orellana'),('PA','Pastaza'),
 		('PI','Pichincha'),('SE','Santa Elena'),('SD','Santo Domingo'),('SU','Sucumbios'),('TU','Tungurahua'),
 		('ZA','Zamora'),)

STA = (	('SO','Soltero/a'),('CA','Casado/a'),('VI','Viudo/a'),('UN','Union Laboral'),)

class CorreoMasivoForm(forms.Form):
	asunto = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
	mensaje = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'5'}))

class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = '__all__'
		widgets = {
 			'img_servicio' : forms.ClearableFileInput(attrs={'class':'form-control'}),
 			'descripcion_pequenia' : forms.Textarea(attrs={'class':'form-control','rows':'3'}),
 			'descripcion_grande' : forms.Textarea(attrs={'class':'form-control','rows':'3'}),
		}
		label = {
			'descripcion_pequenia' : 'Descripción Pequeña',
 			'descripcion_grande' : 'Descripción Grande',
 			'img_servicio' : 'Imagen de servicio',
		}
		error_messages = {
			'tipo' : my_default_errors,
			'descripcion_pequenia' : my_default_errors,
			'descripcion_grande' : my_default_errors,
			'img_servicio' : my_default_errors,
		}

class TipoServicioForm(forms.ModelForm):
	class Meta:
		model = Tipo_servicio
		fields = '__all__'
		widgets = {
			'tipo' : forms.TextInput(attrs={'class':'form-control'}),
		}
		labels = {
			'tipo':'Tipo',
		}
		error_messages = {
			'tipo': my_default_errors,
		}

class TrabajoForm(forms.ModelForm):
	class Meta:
		model = Trabajo
		fields = '__all__'
		widgets = {
			'nombres' : forms.TextInput(attrs={'class':'form-control'}),
			'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
			'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
			'email' : forms.EmailInput(attrs={'class':'form-control'}),
			'direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'convencional' : forms.TextInput(attrs={'class':'form-control'}),
			'celular' : forms.TextInput(attrs={'class':'form-control'}),
		 	'provincia' : forms.Select(choices=PROV, attrs={'class':'form-control'}),
		 	'ciudad' : forms.TextInput(attrs={'class':'form-control'}),
		 	'estado_civil' : forms.Select(choices=STA, attrs={'class':'form-control'}),
		 	'curriculum' : forms.TextInput(attrs={'class':'form-control', 'type':'file'}),
		 	'revisado' : forms.CheckboxInput(attrs={'class':'form-control'}),
		}
		labels = {
			'nombres' : 'Nombres',
			'apellido_paterno' : 'Apellido paterno',
			'apellido_materno' : 'Apellido materno',
			'fecha_nacimiento' : 'Fecha Nacimiento',
			'email' : 'Email',
			'direccion' : 'Dirección',
			'convencional' : 'Convencional',
			'celular' : 'Celular',
		 	'provincia' : 'Provincia',
		 	'ciudad' : 'Ciudad',
		 	'estado_civil' : 'Estado Civil',
		 	'curriculum' : 'Curriculum',
		 	'revisado' : 'Revisado',	
		}
		error_messages = {
			'nombres': my_default_errors,
			'apellido_paterno' : my_default_errors,
			'apellido_materno' : my_default_errors,
			'fecha_nacimiento' : my_default_errors,
			'email' : my_default_errors,
			'direccion' : my_default_errors,
			'convencional' : my_default_errors,
			'celular' : my_default_errors,
			'provincia' : my_default_errors,
			'ciudad': my_default_errors,
			'estado_civil': my_default_errors,
			'curriculum': my_default_errors,
			'revisado': my_default_errors,
		}

class LocalesForm(forms.ModelForm):
	class Meta:
		model = Locales
		fields = '__all__'
		widgets = {
			'razon_social' : forms.TextInput(attrs={'class':'form-control'}),
			'provincia' : forms.Select(choices=PROV, attrs={'class':'form-control'}),
			'ciudad' : forms.TextInput(attrs={'class':'form-control'}),
			'direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'referencias' : forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
			'email' : forms.EmailInput(attrs={'class':'form-control'}),
			'convencional1' : forms.TextInput(attrs={'class':'form-control'}),
			'convencional2' : forms.TextInput(attrs={'class':'form-control'}),
			'celular1' : forms.TextInput(attrs={'class':'form-control'}),
			'celular2' : forms.TextInput(attrs={'class':'form-control'}),
			'mensaje' : forms.Textarea(attrs={'class':'form-control'}),
			'fecha_registro' : forms.DateInput(attrs={'class':'form-control'}),
		}
		labels = {
			'razon_social' : 'Razón Social',
			'provincia' : 'Provincia',
			'ciudad' : 'Ciudad',
			'direccion' : 'Dirección',
			'referencias' : 'Referencias',
			'email' : 'Email',
			'convencional1' : 'Convencional 1',
			'convencional2' : 'Convencional 2',
			'celular1' : 'Celular 1',
			'celular2' : 'Celular 2',
			'mensaje' : 'Mensaje',
			'fecha_registro':'Fecha Registro'
		}
		error_messages = {
			'razon_social': my_default_errors,
			'provincia' : my_default_errors,
			'ciudad' : my_default_errors,
			'direccion' : my_default_errors,
			'referencias' : my_default_errors,
			'email' : my_default_errors,
			'convencional1' : my_default_errors,
			'convencional2' : my_default_errors,
			'celular1' : my_default_errors,
			'celular2' : my_default_errors,
			'mensaje' : my_default_errors,
			'fecha_registro': my_default_errors,
		}

class Ventaja_CompetitivaForm(forms.ModelForm):
	class Meta:
		model = Ventaja_Competitiva
		fields = '__all__'
		widgets = {
			'descripcion' : forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
		}
		labels = {
			'descripcion' : 'Descripción',
		}
		error_messages = {
			'descripcion': my_default_errors,
		}

class ContactoForm(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = '__all__'
		widgets = {
			'nombres_apellidos': forms.TextInput(attrs={'class':'form-control', 'disabled':True}),
		 	'email' : forms.EmailInput(attrs={'class':'form-control','disabled':True}),
		 	'asunto' : forms.TextInput(attrs={'class':'form-control','disabled':True}),
		 	'mensaje' : forms.Textarea(attrs={'class':'form-control', 'rows':'5','disabled':True}),
		 	'fecha' : forms.TextInput(attrs={'class':'form-control'}),
		 	'leido' : forms.CheckboxInput(attrs={'class':'form-control'}),
		}
		labels = {
			'nombres_apellidos': 'Nombres y apellidos',
		 	'email' : 'Email',
		 	'asunto' : 'Asunto',
		 	'mensaje' : 'Mensaje',
		 	'leido' : 'Leído',
		}


class SuscripcionForm(forms.ModelForm):
	class Meta:
		model = Suscripcion
		fields = ['email',]
		widgets = {
			'email' : forms.TextInput(attrs={'class':'form-control'}),
		}
		labels = {
			'email' : 'Email',
		}
		error_messages = {
			'email': my_default_errors,
		}

class ObjetivoForm(forms.ModelForm):
	class Meta:
		model = Objetivo
		fields = '__all__'
		widgets = {
			'tipo': forms.Select(choices=OBJ, attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
		}
		labels = {
			'tipo':'Tipo',
			'descripcion':'Descripción',
		}
		error_messages = {
			'tipo': my_default_errors,
			'descripcion' : my_default_errors,
		}

class TelefonoForm(forms.ModelForm):
	class Meta:
		model = Telefono
		fields = '__all__'
		widgets = {
			'tipo':forms.Select(choices=TYPE, attrs={"class":"form-control"}),
			'operadora':forms.Select(choices=OPER, attrs={"class":'form-control'}),
			'numero':forms.TextInput(attrs={'class':'form-control'}),
		}
		label = {
			'tipo':'Tipo',
			'operadora':'Operadora',
			'numero':'Numero',
		}
		error_messages = {
			'tipo': my_default_errors,
			'operadora' : my_default_errors,
  		 	'numero' : my_default_errors,
		}

class EmpresaForm(forms.ModelForm):
	class Meta:
		model = Empresa
		fields = '__all__'
		widgets = {
			'nombre':forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese el nombre o razón social"}),
			'descripcion':forms.Textarea(attrs={"class":"form-control", "placeholder":"Ingrese la descripción de la empresa", "rows":"5"}),
			'logo' : forms.ClearableFileInput(attrs={'class':'form-control'}),
  		 	'favicon' : forms.ClearableFileInput(attrs={'class':'form-control'}),
  		 	'mision' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese la mision de la empresa', 'rows':'4'}),
  		 	'img_mision' : forms.ClearableFileInput(attrs={'class':'form-control'}),
  		 	'caracteristica1' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese la caracteristica 1 de la empresa'}),
  		 	'caracteristica_descripcion1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese la descripcion de la caracteristica 1 de la empresa', 'rows':'2'}),
  		 	'caracteristica2' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese la caracteristica 2 de la empresa'}),
  		 	'caracteristica_descripcion2' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese la descripcion de la caracteristica 2 de la empresa', 'rows':'2'}),
  		 	'caracteristica3' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese la caracteristica 3 de la empresa'}),
  		 	'caracteristica_descripcion3' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese la descripcion de la caracteristica 3 de la empresa', 'rows':'2'}),
  		 	'caracteristica4': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese la caracteristica 4 de la empresa'}),
  		 	'caracteristica_descripcion4' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese la descripcion de la caracteristica 4 de la empresa', 'rows':'2'}),
  		 	'img_obj1' : forms.ClearableFileInput(attrs={'class':'form-control'}),
  		 	'img_obj2' : forms.ClearableFileInput(attrs={'class':'form-control'}),
  		 	'img_obj3' : forms.ClearableFileInput(attrs={'class':'form-control'}),
  		 	'email' : forms.TextInput(attrs={'type':'email','class':'form-control', 'placeholder':'Ingrese el email de la empresa'}),
  		 	'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese la dirección de la empresa'}),
  		 	'red_facebook' : forms.TextInput(attrs={'type':'url','class':'form-control', 'placeholder':'Ingrese el Facebook de la empresa'}),
  		 	'red_twiiter' : forms.TextInput(attrs={'type':'url','class':'form-control', 'placeholder':'Ingrese el Twitter de la empresa'}),
  		 	'red_instagram' : forms.TextInput(attrs={'type':'url','class':'form-control', 'placeholder':'Ingrese el Instagram de la empresa'}),
		}
		labels = {
			"nombre": "Nombre o Razón Social",
			'descripcion' : 'Descripción',
  		 	'logo' : 'Logo',
  		 	'favicon' : 'Favicon',
  		 	'mision' : 'Misión',
		 	'img_mision' : 'Imagen misión',
  		 	'caracteristica1' : 'Caracteristica 1',
 		 	'caracteristica_descripcion1' : 'Descripción Caracteristica 1',
 		 	'caracteristica2' : 'Caracteristica 2',
  		 	'caracteristica_descripcion2' : 'Descripción Caracteristica 2',
  		 	'caracteristica3' : 'Caracteristica 3',
  		 	'caracteristica_descripcion3' : 'Descripción Caracteristica 3',
  		 	'caracteristica4 ' : 'Caracteristica 4',
 		 	'caracteristica_descripcion4' : 'Descripción Caracteristica 4',
  		 	'img_obj1' : 'Imagen objetivo 1',
  		 	'img_obj2' : 'Imagen objetivo 2',
 		 	'img_obj3' : 'Imagen objetivo 3',
		 	'email' : 'Email',
  		 	'direccion' : 'Dirección',
  		 	'red_facebook' : 'Facebook',
  		 	'red_twiiter' : 'Twitter',
  		 	'red_instagram' : 'Instagram',
		}
		error_messages = {
			'nombre': my_default_errors,
			'descripcion' : my_default_errors,
			'logo' : my_default_errors,
  		 	'favicon' : my_default_errors,
  		 	'mision' : my_default_errors,
  		 	'img_mision' : my_default_errors,
  		 	'caracteristica1' : my_default_errors,
 		 	'caracteristica_descripcion1' : my_default_errors,
 		 	'caracteristica2' : my_default_errors,
  		 	'caracteristica_descripcion2' : my_default_errors,
  		 	'caracteristica3' : my_default_errors,
  		 	'caracteristica_descripcion3' : my_default_errors,
  		 	'caracteristica4 ' : my_default_errors,
 		 	'caracteristica_descripcion4' : my_default_errors,
		 	'img_obj1' : my_default_errors,
  		 	'img_obj2' : my_default_errors,
 		 	'img_obj3' : my_default_errors,
		 	'email' : my_default_errors,
  		 	'direccion' : my_default_errors,
  		 	'red_facebook' : my_default_errors,
  		 	'red_twiiter' : my_default_errors,
  		 	'red_instagram' : my_default_errors,
		}

class LoginForm(forms.Form):

	username = forms.CharField(max_length=30, 
				widget=forms.TextInput(attrs={
					'class':'form-control',
					'placeholder':'Escriba su nombre de usuario'
					}))
	password = forms.CharField(max_length=30,
				widget=forms.PasswordInput(attrs= {
					'class':'form-control',
					'placeholder':'Escriba su contraseña'
					}))