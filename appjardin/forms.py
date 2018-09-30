from django import forms
from .models import Anolectivo, Estudiante, Matricula, Nivel, Paralelo, Pension, Preinscripcion, AuthUser, Profesor, Representante, Rol, Secretaria
from django.forms import ModelForm,TextInput,FileInput,NumberInput,DateInput,Select,CheckboxSelectMultiple,Textarea,ModelMultipleChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class AnolectivoForm(forms.ModelForm):
    class Meta:
        model = Anolectivo
        fields = ['id_anolectivo', 'nombre', 'estado']

class AuthUserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['password', 'username', 'first_name', 'last_name', 'email', 'cedula', 'genero', 'direccion']


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['id_estudiante', 'tipo_sangre', 'alergias', 'id_secretaria','id_representante']


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['id_matricula', 'costo', 'id_preinscripcion', 'id_paralelo']


class NivelForm(forms.ModelForm):
    class Meta:
        model = Nivel
        fields = ['id_nivel', 'id_profesor', 'id_anolectivo' , 'paralelo', 'cupos','nombre']


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
        fields = ['id_preinscripcion', 'id_estudiante', 'id_representante', 'id_nivel', 'id_secretaria']


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['id_profesor', 'imagen', 'titulo_profesor', 'edad', 'ciudad', 'genero', 'celular', 'estado_civil', 'direccion',  'observacion']
        # fields = ('__all__')
        widgets = {
            'observacion': Textarea(attrs={'class':'form-control','placeholder':'Información Adicional', 'width':'100%'}),
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
