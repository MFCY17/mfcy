from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.decorators  import  login_required
from django.utils.decorators  import  method_decorator


@login_required(login_url='/login/')
def representante_estudiante(request):
    est = Matricula.objects.filter(id_preinscripcion__id_estudiante__id_representante__id=request.user.id).order_by('pk')
    ctx = {'object_list':est}
    return render(request,'representantes_estudiantes.html',ctx)

@login_required(login_url='/login/')
def estudiante_profesores(request):
    est = Matricula.objects.filter(id_paralelo__id_profesor__id=request.user.id).order_by('pk')
    ctx = {'object_list':est}
    return render(request,'estudiantes_profesores.html',ctx)

@login_required(login_url='/login/')
def RolesCreate(request):
    if request.method == 'POST':
        form = AuthUserForm(request.POST)
        formS = SecretariaForm(request.POST)
        if form.is_valid():
            if formS.is_valid():
                utl = form.save()
                auth = User.objects.get(pk = utl.pk)
                auth.set_password(utl.password)
                auth.save()
                formR = formS.save(commit=False)
                formR.id = AuthUser.objects.get(id = utl.pk)
                formR.save()
                return redirect('appjardin_representante_create')
    else:
        form = AuthUserForm()
        formS = SecretariaForm()
    return render(request, 'appjardin/secretaria_form.html', {'form': form,'formS':formS})

@login_required(login_url='/login/')
def ProfesoresCreate(request):
    if request.method == 'POST':
        form = AuthUserForm(request.POST)
        formS = ProfesorForm(request.POST, request.FILES)
        if form.is_valid():
            if formS.is_valid():
                utl = form.save()
                auth = User.objects.get(pk = utl.pk)
                auth.set_password(utl.password)
                auth.save()
                formR = formS.save(commit=False)
                formR.id = AuthUser.objects.get(id = utl.pk)
                formR.save()
                return redirect('appjardin_profesor_create')
    else:
        form = AuthUserForm()
        formS = ProfesorForm()
    return render(request, 'appjardin/profesor_form.html', {'form': form,'formS':formS})

@login_required(login_url='/login/')
def AlummoCreate(request):
    if request.method == 'POST':
        form = AuthUserForm(request.POST)
        formS = EstudianteForm(request.POST)
        if form.is_valid():
            if formS.is_valid():
                utl = form.save()
                auth = User.objects.get(pk = utl.pk)
                auth.set_password(utl.password)
                auth.save()
                formR = formS.save(commit=False)
                formR.id = AuthUser.objects.get(id = utl.pk)
                formR.save()
                return redirect('appjardin_estudiante_create')
    else:
        form = AuthUserForm()
        formS = EstudianteForm()
    return render(request, 'appjardin/estudiante_form.html', {'form': form,'formS':formS})

@login_required(login_url='/login/')
def RepresentanteCreateView(request):
    if request.method == 'POST':
        form = AuthUserForm(request.POST)
        formS = RepresentanteForm(request.POST)
        if form.is_valid():
            if formS.is_valid():
                utl = form.save()
                auth = User.objects.get(pk = utl.pk)
                auth.set_password(utl.password)
                auth.save()
                formR = formS.save(commit=False)
                formR.id = AuthUser.objects.get(id = utl.pk)
                formR.save()
                return redirect('appjardin_representante_create')
    else:
        form = AuthUserForm()
        formS = RepresentanteForm()
    return render(request, 'appjardin/representante_form.html', {'form': form,'formS':formS})

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





class RepresentanteDetailView(DetailView):
    model = Representante


class RepresentanteUpdateView(UpdateView):
    model = Representante
    form_class = RepresentanteForm


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
