from . import models
from . import serializers
from rest_framework import viewsets, permissions


class AnolectivoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Anolectivo class"""

    queryset = models.Anolectivo.objects.all()
    serializer_class = serializers.AnolectivoSerializer
    permission_classes = [permissions.IsAuthenticated]


class EstudianteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Estudiante class"""

    queryset = models.Estudiante.objects.all()
    serializer_class = serializers.EstudianteSerializer
    permission_classes = [permissions.IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Matricula class"""

    queryset = models.Matricula.objects.all()
    serializer_class = serializers.MatriculaSerializer
    permission_classes = [permissions.IsAuthenticated]


class NivelViewSet(viewsets.ModelViewSet):
    """ViewSet for the Nivel class"""

    queryset = models.Nivel.objects.all()
    serializer_class = serializers.NivelSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParaleloViewSet(viewsets.ModelViewSet):
    """ViewSet for the Paralelo class"""

    queryset = models.Paralelo.objects.all()
    serializer_class = serializers.ParaleloSerializer
    permission_classes = [permissions.IsAuthenticated]


class PensionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Pension class"""

    queryset = models.Pension.objects.all()
    serializer_class = serializers.PensionSerializer
    permission_classes = [permissions.IsAuthenticated]


class PreinscripcionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Preinscripcion class"""

    queryset = models.Preinscripcion.objects.all()
    serializer_class = serializers.PreinscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfesorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Profesor class"""

    queryset = models.Profesor.objects.all()
    serializer_class = serializers.ProfesorSerializer
    permission_classes = [permissions.IsAuthenticated]


class RepresentanteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Representante class"""

    queryset = models.Representante.objects.all()
    serializer_class = serializers.RepresentanteSerializer
    permission_classes = [permissions.IsAuthenticated]


class RepresentanteestudianteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Representanteestudiante class"""

    queryset = models.Representanteestudiante.objects.all()
    serializer_class = serializers.RepresentanteestudianteSerializer
    permission_classes = [permissions.IsAuthenticated]


class RolViewSet(viewsets.ModelViewSet):
    """ViewSet for the Rol class"""

    queryset = models.Rol.objects.all()
    serializer_class = serializers.RolSerializer
    permission_classes = [permissions.IsAuthenticated]


class SecretariaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Secretaria class"""

    queryset = models.Secretaria.objects.all()
    serializer_class = serializers.SecretariaSerializer
    permission_classes = [permissions.IsAuthenticated]


