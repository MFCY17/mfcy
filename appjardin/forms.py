from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import PasswordInput
from django.forms import TextInput, Textarea

from .models import Anolectivo, Estudiante, Matricula, Nivel, Paralelo, Pension, \
    Preinscripcion, AuthUser, Profesor, Representante, Rol, Secretaria


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,
                                 help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False,
                                help_text='Optional.')
    email = forms.EmailField(max_length=254,
                             help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2',)


class AnolectivoForm(forms.ModelForm):
    class Meta:
        model = Anolectivo
        fields = ['id_anolectivo', 'nombre', 'estado']


class AuthUserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['password', 'username', 'first_name', 'last_name', 'email',
                  'cedula', 'genero', 'direccion']


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['id_estudiante', 'tipo_sangre', 'alergias',
                  'id_representante']

class StudentByRepresentativeForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['id_estudiante', 'tipo_sangre', 'alergias']

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['id_matricula', 'costo', 'id_preinscripcion', 'id_paralelo']


class NivelForm(forms.ModelForm):
    class Meta:
        model = Nivel
        fields = ['id_nivel', 'id_profesor', 'id_anolectivo', 'paralelo',
                  'cupos']


class ParaleloForm(forms.ModelForm):
    class Meta:
        model = Paralelo
        fields = ['id_paralelo', 'id_profesor']


class PensionForm(forms.ModelForm):
    class Meta:
        model = Pension
        fields = ['id_pension', 'costo', 'id_matricula']


class PreinscripcionForm(forms.ModelForm):
    class Meta:
        model = Preinscripcion
        fields = ['id_preinscripcion', 'id_estudiante', 'id_representante',
                  'id_nivel', 'id_secretaria']


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['id_profesor', 'imagen', 'titulo_profesor', 'edad', 'ciudad',
                  'genero', 'celular', 'estado_civil', 'direccion',
                  'observacion']
        # fields = ('__all__')
        widgets = {
            'observacion': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Información Adicional',
                                           'width': '100%'}),
        }


class RepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante
        fields = ['id_representante', 'celular', 'correo']


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['id_rol', 'estudiante', 'profesor', 'id']


class SecretariaForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = ['id_secretaria', 'fecha_ingreso']


class AuthUserRegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['password', 'username', 'email', ]
        widgets = {
            'password': PasswordInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Clave', 'width': '100%'}),
            'username': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Clave',
                       'width': '100%'}),
            'email': TextInput(
                attrs={'class': 'form-control', 'type': 'email',
                       'placeholder': 'Clave', 'width': '100%'})}

    def clean_password(self):
        MIN_LENGTH = getattr(settings, "MIN_LENGTH", None)
        password = self.cleaned_data.get('password')
        if len(password) < MIN_LENGTH:
            raise ValidationError(
                'La clave debe contener al menos %d caracteres.' % (
                    MIN_LENGTH,))
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(
                username=username).count():
            raise forms.ValidationError('Ya existe un usuario con este email.')
        return email

class RepresentanteUserForm(forms.ModelForm):

    class Meta:
        model = Representante
        fields = ['id_representante', 'celular',]

class AuthUserUpdateForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = [ 'first_name', 'last_name', 'email',
                  'cedula', 'genero', 'direccion']
