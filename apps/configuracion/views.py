from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView
from .models import Medicamento , Enfermedad
from .forms import MedicamentoForm , EnfermedadForm , UsuarioForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
# Create your views here.
class ListaEnfermedadView(ListView):
    model = Enfermedad
    template_name = "enfermedad/enfermedad.html"
    context_object_name = 'object_list'
    queryset = Enfermedad.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = super(ListaEnfermedadView, self).get_context_data(**kwargs)
        return context


def BaseGuardar(request, form, template_name, instancia,template_redirect):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            object_list = instancia.filter(estado = True).order_by('descripcion')
            data['message'] = 'Registro guardado con exito'
            data['hide_modal'] = True
            data['form_is_valid'] = True
            data['object_list'] = render_to_string(template_redirect,{'object_list':object_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    print(data)

    return JsonResponse(data)


def CrearEnfermedad(request):
    instancia = Enfermedad.objects
    if request.method == 'POST':
        form = EnfermedadForm(request.POST)
    else:
        form = EnfermedadForm()
    return BaseGuardar(request, form, 'enfermedad/enfermedad_crear.html',instancia,'enfermedad/enfermedad_list.html')


def ActualizarEnfermedad(request, id):
    enfermedad = get_object_or_404(Enfermedad, id=id)
    instancia = Enfermedad.objects
    if request.method == 'POST':
        form = EnfermedadForm(request.POST, instance=enfermedad)
    else:
        form = EnfermedadForm(instance=enfermedad)
    return BaseGuardar(request, form, 'enfermedad/enfermedad_actualizar.html',instancia)


def EliminarEnfermedad(request, id):
    data = dict()
    
    enfermedad = get_object_or_404(Enfermedad, id=id)
    if request.method == 'POST':
        enfermedad.estado = False
        enfermedad.save()
        enfermedades = Enfermedad.objects.filter(estado=True)
        data['form_is_valid'] = True
        data['object_list'] = render_to_string('enfermedad/enfermedad_list.html',{'object_list':enfermedades})
        data['hide_modal'] = True
    else:
        context = {'enfermedad': enfermedad}
        data['html_form'] = render_to_string(
            'enfermedad/enfermedad_eliminar.html', context, request=request)

    return JsonResponse(data)

class ListaMedicamentoView(ListView):
    model = Medicamento
    template_name = "medicamento/medicamento.html"
    context_object_name = 'object_list'
    queryset = Medicamento.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = super(ListaMedicamentoView, self).get_context_data(**kwargs)
        return context

def CrearMedicamento(request):
    instancia = Medicamento.objects
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
    else:
        form = MedicamentoForm()
    return BaseGuardar(request, form, 'medicamento/medicamento_crear.html',instancia,'medicamento/medicamento_list.html')


def ActualizarMedicamento(request, id):
    instancia = Medicamento.objects
    medicamento = get_object_or_404(Medicamento, id=id)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
    else:
        form = MedicamentoForm(instance=medicamento)
    return BaseGuardar(request, form, 'medicamento/medicamento_actualizar.html',instancia,'medicamento/medicamento_list.html')


def EliminarMedicamento(request, id):
    data = dict()
    
    medicamento = get_object_or_404(Medicamento, id=id)
    if request.method == 'POST':
        medicamento.estado = False
        medicamento.save()
        medicamentos = Medicamento.objects.filter(estado=True)
        data['object_list'] = render_to_string('medicamento/medicamento_list.html',{'object_list':medicamentos})
        data['form_is_valid'] = True
        data['hide_modal'] = True
    else:
        context = {'medicamento': medicamento}
        data['html_form'] = render_to_string(
            'medicamento/medicamento_eliminar.html', context, request=request)

    return JsonResponse(data)

class ListaUsuarioView(ListView):
    model = User
    template_name = "usuario/usuario_list.html"
    context_object_name = 'usuario_list'
    queryset = User.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(ListaUsuarioView, self).get_context_data(**kwargs)
        return context

def CrearUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
    else:
        form = UsuarioForm()
    return BaseGuardar(request, form, 'usuario/usuario_crear.html')