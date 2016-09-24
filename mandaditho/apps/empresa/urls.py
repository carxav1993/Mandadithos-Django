from django.conf.urls import include, url


urlpatterns = [
    # Examples:
    # url(r'^$', 'mandaditho.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'apps.empresa.views.inicio', name='inicio'),
    url(r'^inicio/','apps.empresa.views.inicio', name='inicio2'),
    url(r'^empresa/', 'apps.empresa.views.empresa', name='empresa'),
    url(r'^servicios/', 'apps.empresa.views.servicios', name='servicios'),
    url(r'^contactenos/','apps.empresa.views.contactenos',name='contactenos'),
    url(r'^registrate/', 'apps.empresa.views.registrate', name='registrate'),
    
    #coger el ajax para guardar el correo que se suscriben
    url(r'^registro_correo/$','apps.empresa.views.registro_ajax',name='suscripcion_ajax'),
    url(r'^ajax_contacto/$','apps.empresa.views.ajax_contacto',name='ajax_contacto'),
    url(r'^trabajo_ajax/$','apps.empresa.views.trabajo_ajax',name='trabajo_ajax'),
    url(r'^locales_ajax/$','apps.empresa.views.locales_ajax', name='locales_ajax'),

]
