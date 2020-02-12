from django.shortcuts import render
from django.contrib.auth.models import User
from apps.persona.models import Paciente
from django.http import JsonResponse , HttpResponse
import json , csv
# Create your views here.

def HombreMujeresGrafica(request):

    p = Paciente.objects.filter(estado= True).only("sexo")
    mujeres = p.filter(sexo = "F").count()
    hombres = p.filter(sexo = "M").count()
   
    context = {
        "type":"doughnut",        
        "data":{
            "labels":["hombres","mujeres"],
            "datasets":[{
            "data": [hombres,mujeres],
            "backgroundColor": ['#4e73df', '#e487d3'],
            "hoverBackgroundColor": ['#2e59d9', '#e487d3'],
            }]
       }
    }
    return HttpResponse(json.dumps(context))

def ExportaUsuariosCsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Usuario', 'Nombre', 'Apellidos', 'Email'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response

def ExportaPacientesCsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pacientes.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Apellido Paterno', 'Apellido Materno', 'Sexo','Domicilio', 'Telefono'])

    users =     Paciente.objects.all().values_list('nombre', 'ap_paterno', 'ap_materno', 'sexo', 'domicilio','telefono')
    for user in users:
        writer.writerow(user)

    return response