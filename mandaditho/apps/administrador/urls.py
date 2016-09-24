#encoding:utf-8
from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'mandaditho.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'apps.administrador.views.login', name='login'),
    url(r'^login/$', 'apps.administrador.views.login', name='login'),
    url(r'^logout/$','apps.administrador.views.LogOut',name='logout'),
    url(r'^inicio/$', 'apps.administrador.views.inicio', name='inicio'),
    url(r'^empresa/$','apps.administrador.views.empresa',name='empresa'),
    #telefonos
    url(r'^telefonos/anadir_telefono/$','apps.administrador.views.Anadir_Telefono',name='anadir_telefono'),
    url(r'^telefonos/$','apps.administrador.views.telefonos',name='telefonos'),
    url(r'^telefonos/editar_Telefono/(?P<telefono_id>\d+)/$','apps.administrador.views.Editar_Telefono'
        ,name='editar_telefono'),
    url(r'^telefonos/eliminar_telefono/(?P<telefono_id>\d+)/$','apps.administrador.views.Eliminar_Telefono'
        ,name='eliminar_telefono'),

    #objetivos de la empresa
    url(r'^objetivos/anadir_objetivo/$','apps.administrador.views.Anadir_Objetivo',name='anadir_objetivo'),
    url(r'^objetivos/$','apps.administrador.views.Objetivos',name='objetivos'),
    url(r'^objetivos/editar_objetivo/(?P<objetivo_id>\d+)/$','apps.administrador.views.Editar_Objetivos'
        ,name='editar_objetivo'),
    url(r'^objetivos/eliminar_objetivo/(?P<objetivo_id>\d+)/$','apps.administrador.views.Eliminar_Objetivo'
        ,name='eliminar_objetivo'),

    #Suscripciones
    url(r'^suscripciones/anadir_email/$','apps.administrador.views.Anadir_Suscripcion',name='anadir_correo'),
    url(r'^suscripciones/$','apps.administrador.views.Suscripciones',name='suscripciones'),
    url(r'^suscripciones/editar_suscripcion/(?P<suscripcion_id>\d+)/$','apps.administrador.views.Editar_Suscripcion'
        ,name='editar_suscripcion'),
    url(r'suscripcion/eliminar_suscripcion/(?P<suscripcion_id>\d+)/$','apps.administrador.views.Eliminar_Suscripcion'
        ,name='eliminar_suscripcion'),

    ##Contáctenos
    url(r'^contactenos/$','apps.administrador.views.Contactenos',name='contactenos'),
    url(r'^contactenos/ver_contactenos/(?P<contactenos_id>\d+)/$','apps.administrador.views.Ver_Contactenos'
        ,name='ver_contactenos'),
    url(r'^contactenos/eliminar_contactenos/(?P<contactenos_id>\d+)/$','apps.administrador.views.Eliminar_Contactenos'
        ,name='eliminar_contactenos'),

    #Ventajas Competitivas
    url(r'^ventajas/$','apps.administrador.views.Ventajas_Competitivas',name='ventajas_competitivas'),
    url(r'^ventajas/anadir_ventaja/$','apps.administrador.views.Anadir_Ventaja',name='anadir_ventaja'),
    url(r'^ventajas/editar_ventaja/(?P<ventaja_id>\d+)/$','apps.administrador.views.Editar_Ventaja'
        ,name='editar_ventaja'),
    url(r'^ventajas/eliminar_ventaja/(?P<ventaja_id>\d+)/$','apps.administrador.views.Eliminar_Ventaja'
        ,name='eliminar_ventaja'),

    #solicitudes - locales
    url(r'^locales/$','apps.administrador.views.Lista_Locales',name='locales'),
    url(r'^locales/editar_local/(?P<local_id>\d+)/$','apps.administrador.views.Editar_Local',name='editar_local'),
    url(r'^locales/eliminar_local/(?P<local_id>\d+)/$','apps.administrador.views.Eliminar_Local'
        ,name='eliminar_local'),

    #Solicitudes - Trabajo
    url(r'^trabajos/$','apps.administrador.views.Trabajos',name='trabajos'),
    url(r'^trabajos/ver_trabajo/(?P<trabajo_id>\d+)/$','apps.administrador.views.Ver_Trabajo',name='ver_trabajo'),
    url(r'^trabajos/eliminar_trabajo/(?P<trabajo_id>\d+)/$','apps.administrador.views.Eliminar_Trabajo'
        ,name='eliminar_trabajo'),

    #tipos de servicios
    url(r'^tiposServicios/$','apps.administrador.views.Tipos_Servicios',name='tipos_servicios'),
    url(r'^tiposServicios/anadir_tipo/$','apps.administrador.views.Anadir_Tipo',name='anadir_tipo'),
    url(r'^tiposServicios/editar_tipo/(?P<tipo_id>\d+)/$','apps.administrador.views.Editar_Tipo',name='editar_tipo'),
    url(r'^tiposServicios/eliminar_tipo/(?P<tipo_id>\d+)/$','apps.administrador.views.Eliminar_Tipo'
        ,name='eliminar_tipo'),

    #Servicios
    url(r'^servicios/$','apps.administrador.views.Servicios',name='servicios'),
    url(r'^servicios/anadir_servicio/$','apps.administrador.views.Anadir_Servicio',name='anadir_servicio'),
    url(r'^servicios/editar_servicio/(?P<servicio_id>\d+)/$','apps.administrador.views.Editar_Servicio'
        ,name='editar_servicio'),
    url(r'^servicios/eliminar_servicio/(?P<servicio_id>\d+)/$','apps.administrador.views.Eliminar_Servicio',name='eliminar_servicio'),

    #Envio de correo electrónico masivo
    url(r'^suscripciones/correo/$','apps.administrador.views.Correo_Masivo',name='correo_masivo'),
]   