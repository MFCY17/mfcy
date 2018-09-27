from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login, {'template_name': 'index.html'}, name='login'),
    url(r'^login/', login, {'template_name': 'index.html'}, name='login'),
    url(r'^logout/', logout, {'next_page': '/login/'}, name='logout'),
    url(r'^', include('appjardin.urls')),
]
