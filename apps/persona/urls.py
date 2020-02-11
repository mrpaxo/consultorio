from django.urls import path 
from apps.persona.views import ListaPacienteView , CrearPaciente , ActualizarPaciente , EliminarPaciente
from django.contrib.auth.decorators import login_required
urlpatterns =[
    path ('pacientes', login_required(ListaPacienteView.as_view()), name = 'ListaPaciente'),
    path ('pacientes/nuevo', login_required(CrearPaciente), name = 'CrearPaciente'),
    path ('pacientes/<int:id>/actualizar', login_required(ActualizarPaciente), name = 'ActualizarPaciente'),
    path ('pacientes/<int:id>/eliminar', login_required(EliminarPaciente), name = 'EliminarPaciente'),
]