from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Anolectivo, Estudiante, Matricula, Nivel, Paralelo, Pension, Preinscripcion, Profesor, Representante, Representanteestudiante, Rol, Secretaria
from .forms import AnolectivoForm, EstudianteForm, MatriculaForm, NivelForm, ParaleloForm, PensionForm, PreinscripcionForm, ProfesorForm, RepresentanteForm, RepresentanteestudianteForm, RolForm, SecretariaForm


class AnolectivoListView(ListView):
    model = Anolectivo


class AnolectivoCreateView(CreateView):
    model = Anolectivo
    form_class = AnolectivoForm


class AnolectivoDetailView(DetailView):
    model = Anolectivo


class AnolectivoUpdateView(UpdateView):
    model = Anolectivo
    form_class = AnolectivoForm


class EstudianteListView(ListView):
    model = Estudiante


class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm


class EstudianteDetailView(DetailView):
    model = Estudiante


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    form_class = EstudianteForm


class MatriculaListView(ListView):
    model = Matricula


class MatriculaCreateView(CreateView):
    model = Matricula
    form_class = MatriculaForm


class MatriculaDetailView(DetailView):
    model = Matricula


class MatriculaUpdateView(UpdateView):
    model = Matricula
    form_class = MatriculaForm


class NivelListView(ListView):
    model = Nivel


class NivelCreateView(CreateView):
    model = Nivel
    form_class = NivelForm


class NivelDetailView(DetailView):
    model = Nivel


class NivelUpdateView(UpdateView):
    model = Nivel
    form_class = NivelForm


class ParaleloListView(ListView):
    model = Paralelo


class ParaleloCreateView(CreateView):
    model = Paralelo
    form_class = ParaleloForm


class ParaleloDetailView(DetailView):
    model = Paralelo


class ParaleloUpdateView(UpdateView):
    model = Paralelo
    form_class = ParaleloForm


class PensionListView(ListView):
    model = Pension


class PensionCreateView(CreateView):
    model = Pension
    form_class = PensionForm


class PensionDetailView(DetailView):
    model = Pension


class PensionUpdateView(UpdateView):
    model = Pension
    form_class = PensionForm


class PreinscripcionListView(ListView):
    model = Preinscripcion


class PreinscripcionCreateView(CreateView):
    model = Preinscripcion
    form_class = PreinscripcionForm


class PreinscripcionDetailView(DetailView):
    model = Preinscripcion


class PreinscripcionUpdateView(UpdateView):
    model = Preinscripcion
    form_class = PreinscripcionForm


class ProfesorListView(ListView):
    model = Profesor


class ProfesorCreateView(CreateView):
    model = Profesor
    form_class = ProfesorForm


class ProfesorDetailView(DetailView):
    model = Profesor


class ProfesorUpdateView(UpdateView):
    model = Profesor
    form_class = ProfesorForm


class RepresentanteListView(ListView):
    model = Representante


class RepresentanteCreateView(CreateView):
    model = Representante
    form_class = RepresentanteForm


class RepresentanteDetailView(DetailView):
    model = Representante


class RepresentanteUpdateView(UpdateView):
    model = Representante
    form_class = RepresentanteForm


class RepresentanteestudianteListView(ListView):
    model = Representanteestudiante


class RepresentanteestudianteCreateView(CreateView):
    model = Representanteestudiante
    form_class = RepresentanteestudianteForm


class RepresentanteestudianteDetailView(DetailView):
    model = Representanteestudiante


class RepresentanteestudianteUpdateView(UpdateView):
    model = Representanteestudiante
    form_class = RepresentanteestudianteForm


class RolListView(ListView):
    model = Rol


class RolCreateView(CreateView):
    model = Rol
    form_class = RolForm


class RolDetailView(DetailView):
    model = Rol


class RolUpdateView(UpdateView):
    model = Rol
    form_class = RolForm


class SecretariaListView(ListView):
    model = Secretaria


class SecretariaCreateView(CreateView):
    model = Secretaria
    form_class = SecretariaForm


class SecretariaDetailView(DetailView):
    model = Secretaria


class SecretariaUpdateView(UpdateView):
    model = Secretaria
    form_class = SecretariaForm

