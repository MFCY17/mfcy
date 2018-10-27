from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ingresar/$', login, {'template_name': 'index.html'}, name='ingresar'),
    url(r'^service/$', login, {'template_name': 'service.html'}, name='service'),
    url(r'^event/$', login, {'template_name': 'event.html'}, name='event'),
    url(r'^contact/$', login, {'template_name': 'Contactos.html'}, name='contact'),
    url(r'^registrologin/$', login, {'template_name': 'registrologin.html'}, name='registrologin'),
    url(r'^login/', login, {'template_name': 'index.html'}, name='login'),
    url(r'^logout/', logout, {'next_page': '/login/'}, name='logout'),
    url(r'^', include('appjardin.urls')), 
]

