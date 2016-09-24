from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings #para servir imagenes BC:5F:F4:A0:AA:7D

urlpatterns = [
    # Examples:
    # url(r'^$', 'mandaditho.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.empresa.urls', namespace='empresa')),
    url(r'^administrador/', include('apps.administrador.urls', namespace='administrador')),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
	urlpatterns += [
		url(r'^media/(?P<path>.*)$','django.views.static.serve', 
			{'document_root':settings.MEDIA_ROOT,}
		),
	]