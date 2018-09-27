from django.conf import settings
from django.contrib import auth
from .models import Profesor,Representante,Secretaria
from django.utils.deprecation import MiddlewareMixin

class UserTZMiddleware(MiddlewareMixin):
    def process_view(self,request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated():
            try:
                prof = Profesor.objects.get(id=request.user.id)
                request.user.profesor = True
            except Profesor.DoesNotExist:
                request.user.profesor = False
            try:
                rep = Representante.objects.get(id=request.user.id)
                request.user.representante = True
            except Representante.DoesNotExist:
                request.user.representante = False
            try:
                sec = Secretaria.objects.get(id=request.user.id)
                request.user.secretaria = True
            except Secretaria.DoesNotExist:
                request.user.secretaria = False
