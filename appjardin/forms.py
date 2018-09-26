from django import forms
from .models import Anolectivo, Estudiante, Matricula, Nivel, Paralelo, Pension, Preinscripcion, Profesor, Representante, Representanteestudiante, Rol, Secretaria


class AnolectivoForm(forms.ModelForm):
    class Meta:
        model = Anolectivo
        fields = ['id_anolectivo', 'nombre', 'estado']


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['id_estudiante', 'tipo_sangre', 'alergias', 'id_secretaria', 'id']


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['id_matricula', 'costo', 'fecha', 'id_preinscripcion', 'id_paralelo']


class NivelForm(forms.ModelForm):
    class Meta:
        model = Nivel
        fields = ['id_nivel', 'nombre', 'id_anolectivo']


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
        fields = ['id_preinscripcion', 'fecha', 'id_estudiante', 'id_representante', 'id_nivel', 'id_secretaria']


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['id_profesor', 'titulo_profesor', 'celular', 'estado_civil', 'id']


class RepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante
        fields = ['id_representante', 'celular', 'correo', 'id']


class RepresentanteestudianteForm(forms.ModelForm):
    class Meta:
        model = Representanteestudiante
        fields = ['id_representanteestudiante', 'id_estudiante', 'id_representante']


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['id_rol', 'estudiante', 'profesor', 'id']


class SecretariaForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = ['id_secretaria', 'fecha_ingreso', 'id']


