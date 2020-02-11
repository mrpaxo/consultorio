from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .forms import CitaForm
from apps.cita.models import Cita
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.http import JsonResponse ,HttpResponse
import json
# Create your views here.

class MuestraCitas(TemplateView):
    template_name = 'citas.html'
    # aqui se va a consultar el estado del sistema (abierto o cerrado)

    def get_context_data(self, **kwargs):
        context = super(MuestraCitas, self).get_context_data(**kwargs)

        return context

def BaseCitas(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['hide_modal'] = True
            data['form_is_valid'] = True
        else:
            print('formulario invalido')
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)

    return JsonResponse(data)

def Citas(request):
    events_list =[]
    for cita in Cita.objects.filter(status=1):
        event = {
            "id": cita.pk,
            "title": cita.paciente.nombre,
            "start":str(cita.inicio),
            "color":cita.color
        }
        events_list.append(event)
    #return JsonResponse(json.dumps(events_list))
    return HttpResponse(json.dumps(events_list))

def CrearCita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
    else:
        form = CitaForm()
    return BaseCitas(request, form, 'cita_crear.html')

def ActualizarCita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
    else:
        form = CitaForm(instance=cita)
    return BaseCitas(request, form, 'cita_actualizar.html')


