from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView
from .models import Paciente
from .forms import PacienteForm
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.


class ListaPacienteView(ListView):
    model = Paciente
    template_name = "paciente/paciente.html"
    context_object_name = 'object_list'
    queryset = Paciente.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = super(ListaPacienteView, self).get_context_data(**kwargs)
        return context


def BasePaciente(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['message'] = 'Paciente guardado con exito'
            data['hide_modal'] = True
            data['form_is_valid'] = True
            pacientes = Paciente.objects.filter(estado=True)
            data['object_list'] = render_to_string('paciente/paciente_list.html',{'object_list':pacientes})
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def CrearPaciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
    else:
        form = PacienteForm()
    return BasePaciente(request, form, 'paciente/paciente_crear.html')


def ActualizarPaciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
    else:
        form = PacienteForm(instance=paciente)
    return BasePaciente(request, form, 'paciente/paciente_actualizar.html')


def EliminarPaciente(request, id):
    data = dict()
    
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.estado = False
        paciente.save()
        data['form_is_valid'] = True
        data['hide_modal'] = True
        paciente = Paciente.objects.filter(estado=True)
        data['object_list'] = render_to_string('paciente/paciente_list.html',{'object_list':paciente})
        
    else:
        
        context = {'paciente': paciente}
        data['html_form'] = render_to_string('paciente/paciente_eliminar.html', context, request=request)

    return JsonResponse(data)
