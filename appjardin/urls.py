# from django.conf.urls import url, include
from django.conf.urls import *
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
# from . import api
from django.views.generic.base import TemplateView

# router = routers.DefaultRouter()
# router.register(r'anolectivo', api.AnolectivoViewSet)
# router.register(r'estudiante', api.EstudianteViewSet)
# router.register(r'matricula', api.MatriculaViewSet)
# router.register(r'nivel', api.NivelViewSet)
# router.register(r'paralelo', api.ParaleloViewSet)
# router.register(r'pension', api.PensionViewSet)
# router.register(r'preinscripcion', api.PreinscripcionViewSet)
# router.register(r'profesor', api.ProfesorViewSet)
# router.register(r'representante', api.RepresentanteViewSet)
# router.register(r'rol', api.RolViewSet)
# router.register(r'secretaria', api.SecretariaViewSet)

urlpatterns = [
    # urls for Django Rest Framework API
    # url(r'^api/v1/', include(router.urls)),
    url(r'inicio/$', TemplateView.as_view(template_name='base.html'), name ='inicio'),
    url(r'^rol/$', views.RolesCreate, name='RolesCreate'),
    url(r'^representante/estudiantes/$', views.representante_estudiante, name='representante_estudiante'),
    url(r'^profesores/estudiante$', views.estudiante_profesores, name='estudiante_profesores'),
    # urls for Anolectivo
    url(r'^appjardin/anolectivo/$', views.AnolectivoListView.as_view(), name='appjardin_anolectivo_list'),
    url(r'^appjardin/anolectivo/create/$', views.AnolectivoCreateView.as_view(), name='appjardin_anolectivo_create'),
    url(r'^appjardin/anolectivo/detail/(?P<pk>\S+)/$', views.AnolectivoDetailView.as_view(), name='appjardin_anolectivo_detail'),
    url(r'^appjardin/anolectivo/update/(?P<pk>\S+)/$', views.AnolectivoUpdateView.as_view(), name='appjardin_anolectivo_update'),
    # urls for Estudiante
    url(r'^appjardin/estudiante/$', views.EstudianteListView.as_view(), name='appjardin_estudiante_list'),
    url(r'^appjardin/estudiante/create/$', views.AlummoCreate, name='appjardin_estudiante_create'),
    url(r'^appjardin/estudiante/detail/(?P<pk>\S+)/$', views.EstudianteDetailView.as_view(), name='appjardin_estudiante_detail'),
    url(r'^appjardin/estudiante/update/(?P<pk>\S+)/$', views.EstudianteUpdateView.as_view(), name='appjardin_estudiante_update'),
    # urls for Matricula
    url(r'^appjardin/matricula/$', views.MatriculaListView.as_view(), name='appjardin_matricula_list'),
    url(r'^appjardin/matricula/create/$', views.MatriculaCreateView.as_view(), name='appjardin_matricula_create'),
    url(r'^appjardin/matricula/detail/(?P<pk>\S+)/$', views.MatriculaDetailView.as_view(), name='appjardin_matricula_detail'),
    url(r'^appjardin/matricula/update/(?P<pk>\S+)/$', views.MatriculaUpdateView.as_view(), name='appjardin_matricula_update'),
    # urls for Nivel
    url(r'^appjardin/nivel/$', views.NivelListView.as_view(), name='appjardin_nivel_list'),
    url(r'^appjardin/nivel/create/$', views.NivelCreateView.as_view(), name='appjardin_nivel_create'),
    url(r'^appjardin/nivel/detail/(?P<pk>\S+)/$', views.NivelDetailView.as_view(), name='appjardin_nivel_detail'),
    url(r'^appjardin/nivel/update/(?P<pk>\S+)/$', views.NivelUpdateView.as_view(), name='appjardin_nivel_update'),
    # urls for Paralelo
    url(r'^appjardin/paralelo/$', views.ParaleloListView.as_view(), name='appjardin_paralelo_list'),
    url(r'^appjardin/paralelo/create/$', views.ParaleloCreateView.as_view(), name='appjardin_paralelo_create'),
    url(r'^appjardin/paralelo/detail/(?P<pk>\S+)/$', views.ParaleloDetailView.as_view(), name='appjardin_paralelo_detail'),
    url(r'^appjardin/paralelo/update/(?P<pk>\S+)/$', views.ParaleloUpdateView.as_view(), name='appjardin_paralelo_update'),
    # urls for Pension
    url(r'^appjardin/pension/$', views.PensionListView.as_view(), name='appjardin_pension_list'),
    url(r'^appjardin/pension/create/$', views.PensionCreateView.as_view(), name='appjardin_pension_create'),
    url(r'^appjardin/pension/detail/(?P<pk>\S+)/$', views.PensionDetailView.as_view(), name='appjardin_pension_detail'),
    url(r'^appjardin/pension/update/(?P<pk>\S+)/$', views.PensionUpdateView.as_view(), name='appjardin_pension_update'),
    # urls for Preinscripcion
    url(r'^appjardin/preinscripcion/$', views.PreinscripcionListView.as_view(), name='appjardin_preinscripcion_list'),
    url(r'^appjardin/preinscripcion/create/$', views.PreinscripcionCreateView.as_view(), name='appjardin_preinscripcion_create'),
    url(r'^appjardin/preinscripcion/detail/(?P<pk>\S+)/$', views.PreinscripcionDetailView.as_view(), name='appjardin_preinscripcion_detail'),
    url(r'^appjardin/preinscripcion/update/(?P<pk>\S+)/$', views.PreinscripcionUpdateView.as_view(), name='appjardin_preinscripcion_update'),
    # urls for Profesor
    url(r'^appjardin/profesor/$', views.ProfesorListView.as_view(), name='appjardin_profesor_list'),
    url(r'^appjardin/profesor/create/$', views.ProfesoresCreate, name='appjardin_profesor_create'),
    url(r'^appjardin/profesor/detail/(?P<pk>\S+)/$', views.ProfesorDetailView.as_view(), name='appjardin_profesor_detail'),
    url(r'^appjardin/profesor/update/(?P<pk>\S+)/$', views.ProfesorUpdateView.as_view(), name='appjardin_profesor_update'),
    # urls for Representante
    url(r'^appjardin/representante/$', views.RepresentanteListView.as_view(), name='appjardin_representante_list'),
    url(r'^appjardin/representante/create/$', views.RepresentanteCreateView, name='appjardin_representante_create'),
    url(r'^appjardin/representante/detail/(?P<pk>\S+)/$', views.RepresentanteDetailView.as_view(), name='appjardin_representante_detail'),
    url(r'^appjardin/representante/update/(?P<pk>\S+)/$', views.RepresentanteUpdateView.as_view(), name='appjardin_representante_update'),
    # urls for Rol
    url(r'^appjardin/rol/$', views.RolListView.as_view(), name='appjardin_rol_list'),
    url(r'^appjardin/rol/create/$', views.RolCreateView.as_view(), name='appjardin_rol_create'),
    url(r'^appjardin/rol/detail/(?P<pk>\S+)/$', views.RolDetailView.as_view(), name='appjardin_rol_detail'),
    url(r'^appjardin/rol/update/(?P<pk>\S+)/$', views.RolUpdateView.as_view(), name='appjardin_rol_update'),
    # urls for Secretaria
    url(r'^appjardin/secretaria/$', views.SecretariaListView.as_view(), name='appjardin_secretaria_list'),
    url(r'^appjardin/secretaria/create/$', views.SecretariaCreateView.as_view(), name='appjardin_secretaria_create'),
    url(r'^appjardin/secretaria/detail/(?P<pk>\S+)/$', views.SecretariaDetailView.as_view(), name='appjardin_secretaria_detail'),
    url(r'^appjardin/secretaria/update/(?P<pk>\S+)/$', views.SecretariaUpdateView.as_view(), name='appjardin_secretaria_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
# 	url(r'^$', views.index, name='index'),
# ]
