from django.contrib import admin
from .models import Empresa, Telefono, Objetivo, Tipo_servicio, Servicio, Suscripcion, Contacto, Ventaja_Competitiva, Trabajo, Locales, ImagenesPublicidad

#Register your models here.
admin.site.register(Empresa)
admin.site.register(Telefono)
admin.site.register(Objetivo)
admin.site.register(Tipo_servicio)
admin.site.register(Servicio)
admin.site.register(Suscripcion)
admin.site.register(Contacto)
admin.site.register(Ventaja_Competitiva)
admin.site.register(Trabajo)
admin.site.register(Locales)
admin.site.register(ImagenesPublicidad)