#encoding:utf-8
from django import forms
from .models import Trabajo, Locales

class TrabajoForm(forms.Form):
	PROV = (('AZ','Azuay'),	('BO','Bolivar'), ('CA','Cañar'), ('CR','Carchi'), ('CH','Chimborazo'), ('CO','Cotopaxi'),
 		('OR','El Oro'), ('ES','Esmeraldas'), ('GA','Galápagos'), ('GU','Guayas'), ('IM','Imbabura'), ('LO','Loja'),
 		('LR','Los Rios'), ('MA','Manabi'), ('MS','Morona Santiago'), ('NA','Napo'), ('OR','Orellana'), ('PA','Pastaza'),
 		('PI','Pichincha'), ('SE','Santa Elena'), ('SD','Santo Domingo'), ('SU','Sucumbios'), ('TU','Tungurahua'),
 		('ZA','Zamora'), )
	STA = ( ('SO','Soltero/a'), ('CA','Casado/a'), ('VI','Viudo/a'), ('UN','Union Laboral'), )

	nombres = forms.CharField(label='Nombres',max_length=50, widget=forms.TextInput(attrs={'class': 'campos'}))
	apellidos_paterno = forms.CharField(label='Apellido paterno',max_length=50, widget=forms.TextInput(attrs={'class': 'campos'}))
	apellidos_materno = forms.CharField(label='Apellido materno',max_length=50, widget=forms.TextInput(attrs={'class': 'campos'}))
	fecha_nacimiento = forms.DateField(label='Fecha Nacimiento', widget=forms.DateInput(attrs={'class': 'campos', 'type':'date'}))
	email = forms.EmailField(label='Su email', widget=forms.EmailInput(attrs={'class': 'campos', 'placeholder':'ejemplo@dominio.com'}))
	direccion = forms.CharField(label='Dirección', max_length=255, widget=forms.Textarea(attrs={'class': 'campos', 'rows':'2'}))
	convencional = forms.CharField(label='Telf. Convencional', max_length=15, widget=forms.TextInput(attrs={'class': 'campos', 'placeholder':'(XX)-XXXXXXX'}))
	celular = forms.CharField(label='Telf. Celular', max_length=10, widget=forms.TextInput(attrs={'class': 'campos', 'placeholder':'09XXXXXXXX'}))
	provincia = forms.CharField(label='Provincia', max_length=50,
									widget=forms.Select(choices=PROV, attrs={'class':'campos'}))
	ciudad = forms.CharField(label='Ciudad',max_length=75, widget=forms.TextInput(attrs={'class': 'campos'}))
	estado_civil = forms.CharField(label='Esado civil', max_length=50,
									widget=forms.Select(choices=STA, attrs={'class':'campos'}))
	curriculum = forms.FileField(label='Su curriculum', widget=forms.FileInput(attrs={'class': 'campos'}))

	
#Este código corresponde a la creación de un modelForm
	# class Meta:
	# 	model = Trabajo
	# 	exclude = ['fecha_solicitud', 'revisado']
	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
 #        for field in self.fields:
 #            # Recorremos todos los campos del modelo para añadirle class="form-control
 #            fields[field].widget.attrs.update({'class': 'form-control'})

class LocalesForm(forms.Form):
	# class Meta:
	# 	model = Locales
	# 	exclude = ['fecha_registro',]
	PROV = (('AZ','Azuay'),	('BO','Bolivar'), ('CA','Cañar'), ('CR','Carchi'), ('CH','Chimborazo'), ('CO','Cotopaxi'),
 		('OR','El Oro'), ('ES','Esmeraldas'), ('GA','Galápagos'), ('GU','Guayas'), ('IM','Imbabura'), ('LO','Loja'),
 		('LR','Los Rios'), ('MA','Manabi'), ('MS','Morona Santiago'), ('NA','Napo'), ('OR','Orellana'), ('PA','Pastaza'),
 		('PI','Pichincha'), ('SE','Santa Elena'), ('SD','Santo Domingo'), ('SU','Sucumbios'), ('TU','Tungurahua'),
 		('ZA','Zamora'), )

	razon_social = forms.CharField(label='Razon Social',max_length=100, widget=forms.TextInput(attrs={'class':'campos'}))
	provincia = forms.CharField(label='Provincia',max_length=50, widget=forms.Select(choices=PROV, attrs={'class':'campos'}))
	ciudad = forms.CharField(label='Ciudad',max_length=50, widget=forms.TextInput(attrs={'class':'campos'}))
	direccion = forms.CharField(label='Dirección',max_length=255, widget=forms.Textarea(attrs={'class':'campos', 'rows':'2'}))
	referencias = forms.CharField(label='Referencias',max_length=255, widget=forms.Textarea(attrs={'class':'campos', 'rows':'2'}))
	email = forms.EmailField(label='Su email', widget=forms.EmailInput(attrs={'class':'campos','placeholder':'ejemplo@dominio.com'}))
	convencional1 = forms.CharField(label='Convencional 1',max_length=15, widget=forms.TextInput(attrs={'class':'campos','placeholder':'(XX)-XXXXXXX'}))
	convencional2 = forms.CharField(label='Convencional 2',max_length=15, widget=forms.TextInput(attrs={'class':'campos','placeholder':'(XX)-XXXXXXX'}))
	celular1 = forms.CharField(label='Celular 1',max_length=10, widget=forms.TextInput(attrs={'class':'campos','placeholder':'09XXXXXXXX'}))
	celular2 = forms.CharField(label='Celular 2',max_length=10, widget=forms.TextInput(attrs={'class':'campos','placeholder':'09XXXXXXXX'}))
	mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class':'campos', 'rows':'2'}))