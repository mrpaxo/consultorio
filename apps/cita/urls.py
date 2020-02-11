from django.urls import path 
from apps.cita.views import CrearCita ,ActualizarCita,Citas , MuestraCitas
from django.contrib.auth.decorators import login_required

urlpatterns =[
 
 path ('citas', login_required(MuestraCitas.as_view()), name = 'MuestraCitas'),
 path ('citas/nuevo', login_required(CrearCita), name = 'CrearCita'),
 path ('citas/<int:id>/actualizar', login_required(ActualizarCita), name = 'ActualizarCita'),
 path ('citas/lista', login_required(Citas), name = 'ListaCitas')
]