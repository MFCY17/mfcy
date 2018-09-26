from . import models

from rest_framework import serializers


class AnolectivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Anolectivo
        fields = (
            'pk', 
            'id_anolectivo', 
            'nombre', 
            'estado', 
        )


class EstudianteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Estudiante
        fields = (
            'pk', 
            'id_estudiante', 
            'tipo_sangre', 
            'alergias', 
            'id_secretaria', 
        )


class MatriculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Matricula
        fields = (
            'pk', 
            'id_matricula', 
            'costo', 
            'fecha', 
        )


class NivelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Nivel
        fields = (
            'pk', 
            'id_nivel', 
            'nombre', 
        )


class ParaleloSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Paralelo
        fields = (
            'pk', 
            'id_paralelo', 
        )


class PensionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pension
        fields = (
            'pk', 
            'id_pension', 
            'costo', 
        )


class PreinscripcionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Preinscripcion
        fields = (
            'pk', 
            'id_preinscripcion', 
            'fecha', 
        )


class ProfesorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profesor
        fields = (
            'pk', 
            'id_profesor', 
            'titulo_profesor', 
            'celular', 
            'estado_civil', 
        )


class RepresentanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Representante
        fields = (
            'pk', 
            'id_representante', 
            'celular', 
            'correo', 
        )


class RepresentanteestudianteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Representanteestudiante
        fields = (
            'pk', 
            'id_representanteestudiante', 
        )


class RolSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rol
        fields = (
            'pk', 
            'id_rol', 
            'estudiante', 
            'profesor', 
        )


class SecretariaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Secretaria
        fields = (
            'pk', 
            'id_secretaria', 
            'fecha_ingreso', 
        )


