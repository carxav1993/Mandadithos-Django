#encoding:utf-8
from django.db import models

# Create your models here.
class Empresa (models.Model):
 	nombre = models.CharField(max_length=50)
 	descripcion = models.TextField()
 	logo = models.ImageField(upload_to='empresa/empresa')
 	favicon = models.ImageField(upload_to='empresa/empresa')
 	mision = models.TextField()
 	img_mision = models.ImageField(upload_to='empresa/empresa')
 	caracteristica1 = models.CharField(max_length=100)
 	caracteristica_descripcion1 = models.TextField()
 	caracteristica2 = models.CharField(max_length=100)
 	caracteristica_descripcion2 = models.TextField()
 	caracteristica3 = models.CharField(max_length=100)
 	caracteristica_descripcion3 = models.TextField()
 	caracteristica4 = models.CharField(max_length=100)
 	caracteristica_descripcion4 = models.TextField()
 	img_obj1 = models.ImageField(upload_to='empresa/objetivos')
 	img_obj2 = models.ImageField(upload_to='empresa/objetivos')
 	img_obj3 = models.ImageField(upload_to='empresa/objetivos')
 	email = models.EmailField()
 	direccion = models.CharField(max_length=155)
 	red_facebook = models.URLField()
 	red_twiiter = models.URLField()
 	red_instagram = models.URLField()

 	def __unicode__(self):
 		return self.nombre

class Telefono(models.Model):
 	TYPE = (
 		('CN','Convencional'),
 		('CL','Celular'),
 	)
 	OPER = (
 		('CL','Claro'),
 		('MO','Movistar'),
 		('CNT','CNT'),
 		('TW','Tuenti'),
 	)
 	tipo = models.CharField(max_length=50, choices=TYPE)
 	operadora = models.CharField(max_length=50, choices=OPER)
 	numero = models.CharField(max_length=50)

 	def __unicode__(self):
 		return "%s %s %s" % (self.tipo, self.numero, self.operadora)

class Objetivo(models.Model):
 	OBJ = (
 		('LP','Largo Plazo'),
 		('MP','Mediano Plazo'),
 		('CP','Corto Plazo'),
 	)
 	tipo = models.CharField(max_length=50, choices=OBJ)
 	descripcion = models.TextField()
	 	
 	def __unicode__(self):
 		return "%s %s" %(self.tipo, self.descripcion)

class Tipo_servicio(models.Model):
 	tipo = models.CharField(max_length=155)
	def __unicode__(self):
 		return self.tipo

class Servicio(models.Model):
 	tipo = models.ForeignKey(Tipo_servicio)
 	descripcion_pequenia = models.CharField(max_length=255)
 	descripcion_grande = models.TextField()
 	img_servicio = models.ImageField(upload_to='empresa/servicios')

	def __unicode__(self):
 		return "%s %s" % (self.tipo.tipo, self.descripcion_pequenia)

class Suscripcion(models.Model):
 	email = models.EmailField()
 	fecha = models.DateField(auto_now_add=True)

 	def __unicode__(self):
 		return "%s %s" % (self.email, self.fecha)

class Contacto(models.Model):
 	nombres_apellidos = models.CharField(max_length=155)
 	email = models.EmailField()
 	asunto = models.CharField(max_length=155)
 	mensaje = models.TextField()
 	fecha = models.DateField(auto_now_add=True)
 	leido = models.BooleanField(default=False)

 	def __unicode__(self):
 		return "%s %s" % (self.nombres_apellidos, self.asunto)

class Ventaja_Competitiva(models.Model):
	descripcion = models.TextField()

	def __unicode__(self):
		return self.descripcion

class Locales(models.Model):
	PROV = (
 		('AZ','Azuay'),
 		('BO','Bolivar'),
 		('CA','Cañar'),
 		('CR','Carchi'),
 		('CH','Chimborazo'),
 		('CO','Cotopaxi'),
 		('OR','El Oro'),
 		('ES','Esmeraldas'),
 		('GA','Galápagos'),
 		('GU','Guayas'),
 		('IM','Imbabura'),
 		('LO','Loja'),
 		('LR','Los Rios'),
 		('MA','Manabi'),
 		('MS','Morona Santiago'),
 		('NA','Napo'),
 		('OR','Orellana'),
 		('PA','Pastaza'),
 		('PI','Pichincha'),
 		('SE','Santa Elena'),
 		('SD','Santo Domingo'),
 		('SU','Sucumbios'),
 		('TU','Tungurahua'),
 		('ZA','Zamora'),
 	)
	razon_social = models.CharField(max_length=100)
	provincia = models.CharField(max_length=50, choices=PROV)
	ciudad = models.CharField(max_length=50)
	direccion = models.CharField(max_length=255)
	referencias = models.CharField(max_length=255)
	email = models.EmailField(blank=True, null=True)
	convencional1 = models.CharField(max_length=15, blank=True, null=True)
	convencional2 = models.CharField(max_length=15, blank=True, null=True)
	celular1 = models.CharField(max_length=10)
	celular2 = models.CharField(max_length=10, blank=True, null=True)
	mensaje = models.TextField()

	fecha_registro = models.DateField(auto_now_add=True)


	def __unicode__(self):
		return "%s %s %s" % (self.razon_social, self.ciudad, self.fecha_registro)

class Trabajo(models.Model):
	PROV = (
 		('AZ','Azuay'),
 		('BO','Bolivar'),
 		('CA','Cañar'),
 		('CR','Carchi'),
 		('CH','Chimborazo'),
 		('CO','Cotopaxi'),
 		('OR','El Oro'),
 		('ES','Esmeraldas'),
 		('GA','Galápagos'),
 		('GU','Guayas'),
 		('IM','Imbabura'),
 		('LO','Loja'),
 		('LR','Los Rios'),
 		('MA','Manabi'),
 		('MS','Morona Santiago'),
 		('NA','Napo'),
 		('OR','Orellana'),
 		('PA','Pastaza'),
 		('PI','Pichincha'),
 		('SE','Santa Elena'),
 		('SD','Santo Domingo'),
 		('SU','Sucumbios'),
 		('TU','Tungurahua'),
 		('ZA','Zamora'),
 	)
	STA = (
		('SO','Soltero/a'),
		('CA','Casado/a'),
		('VI','Viudo/a'),
		('UN','Union Laboral'),
	)
	nombres = models.CharField(max_length=100)
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	email = models.EmailField()
	direccion = models.CharField(max_length=255)
	convencional = models.CharField(max_length=15, null=True, blank=True)
	celular = models.CharField(max_length=10)
 	provincia = models.CharField(max_length=50, choices=PROV)
 	ciudad = models.CharField(max_length=75)
 	estado_civil = models.CharField(max_length=50, choices=STA)
 	curriculum = models.FileField(upload_to='empresa/curriculums')

 	fecha_solicitud = models.DateField(auto_now_add=True)
 	revisado = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s %s %s %s" % (self.nombres, self.apellido_paterno, self.ciudad, self.fecha_solicitud)

class ImagenesPublicidad(models.Model):
	imagen = models.ImageField(upload_to='empresa/publicidad')

	def __unicode__(self):
		return "%s" %self.imagen