from django.shortcuts import render, get_object_or_404
from .models import Consulta , Receta ,RecetaDescripcion
from .forms import ConsultaForm , RecetaDescripcionForm ,RecetaForm
from django.http import JsonResponse
from django.views.generic import ListView , DetailView
from django.template.loader import render_to_string


class ListaConsultaView(ListView):
    model = Consulta
    template_name = "consulta/consulta.html"
    context_object_name = 'object_list'
    queryset = Consulta.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = super(ListaConsultaView, self).get_context_data(**kwargs)
        return context


def BaseGuardar(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
             
            data['hide_modal'] = True
            data['form_is_valid'] = True
            consulta = Consulta.objects.filter(estado = True)
            data['object_list'] = render_to_string('consulta/consulta_list.html',{'object_list':consulta})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def CrearConsulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
    else:
        form = ConsultaForm()
    return BaseGuardar(request, form, 'consulta/consulta_crear.html')


def ActualizarConsulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
    else:
        form = ConsultaForm(instance=consulta)
    return BaseGuardar(request, form, 'consulta/consulta_actualizar.html')


def EliminarConsulta(request, id):
    data = dict()
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        consulta.estado = False
        consulta.save()
        consulta = Consulta.objects.filter(estado=True)
        data['object_list'] = render_to_string('consulta/consulta_list.html',{'object_list':consulta})
        data['form_is_valid'] = True
        data['hide_modal'] = True
    else:
        context = {'consulta': consulta}
        data['html_form'] = render_to_string(
            'consulta/consulta_eliminar.html', context, request=request)

    return JsonResponse(data)


def ActualizarReceta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=consulta)
    else:
        form = RecetaForm(instance=consulta)
    return BaseGuardar(request, form, 'receta/receta_actualizar.html')
        


def CrearReceta(request, id):
    data = dict()
    lista_receta  = []
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'GET':
        if consulta.receta:
            data['hidden_field'] = [{'nombre':'receta_id','valor':consulta.receta.id},{'nombre':'consulta_id','valor':consulta.id}]
            lista_receta = consulta.receta.descripcion.all()
        else:
            r = Receta.objects.create(doctor=request.user)
            consulta.receta = r
            consulta.save()
            data['hidden_field'] = [{'nombre':'receta_id','valor':r.id},{'nombre':'consulta_id','valor':consulta.id}]
        data['extra_function'] = True
        data['form_is_valid'] = True
        form = RecetaDescripcionForm()
    else:
        form = RecetaForm()
    context = {'form': form, 'lista_receta':lista_receta}
    data['html_form'] = render_to_string('receta/receta_actualizar.html', context, request=request)

    return JsonResponse(data)


def CrearRecetaDescripcion(request):
    data = dict()
    lista_receta  = []
    if request.method == 'POST':
        form = RecetaDescripcionForm(request.POST)
        if form.is_valid():        
            try:
                r = RecetaDescripcion.objects.create(medicamento = form.cleaned_data['medicamento'], indicacion = form.cleaned_data['indicacion'])
                receta_id = request.POST.get('receta_id')
                receta = Receta.objects.get(id=receta_id)
                receta.descripcion.add(r)
                lista_receta = receta.descripcion.all()                
            except Exception as e:
                print(e)
            data['form_is_valid'] = True
            data['hide_modal'] = False
            data['extra_function'] = True#ejecutar una funcion generica , que necesite informacion extra , para generar contenido dinamico
            data['receta_descripcion'] = {'id':r.id,'medicamento':r.medicamento.descripcion,'indicacion':r.indicacion}
            form = RecetaDescripcionForm()
        else:
            data['form_is_valid']= False
            
    else:
        form = RecetaForm()
    context = {'form': form, 'lista_receta':lista_receta}
    data['html_form'] = render_to_string('receta/receta_actualizar.html', context, request=request)

    return JsonResponse(data)

def EliminarRecetaDescripcion(request, id):
    data = dict()
    try:
        RecetaDescripcion.objects.get(pk=id).delete()
        data['form_is_valid'] = True
    except Exception as e:
        data['form_is_valid'] = False
        print(e)

    return JsonResponse(data)

class ConsultaDetailView(DetailView):
    template_name = "receta/receta.html"
    model = Consulta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context