from django.urls import path 
from apps.configuracion.views import ListaEnfermedadView , CrearEnfermedad , ActualizarEnfermedad , EliminarEnfermedad , ListaMedicamentoView , CrearMedicamento , ActualizarMedicamento , EliminarMedicamento, ListaUsuarioView, CrearUsuario
from django.contrib.auth.decorators import login_required
urlpatterns =[
    path ('enfermedades', login_required(ListaEnfermedadView.as_view()), name = 'ListaEnfermedad'),
    path ('enfermedades/nuevo', login_required(CrearEnfermedad), name = 'CrearEnfermedad'),
    path ('enfermedades/<int:id>/actualizar', login_required(ActualizarEnfermedad), name = 'ActualizarEnfermedad'),
    path ('enfermedades/<int:id>/eliminar', login_required(EliminarEnfermedad), name = 'EliminarEnfermedad'),

    path ('medicamentos', login_required(ListaMedicamentoView.as_view()), name = 'ListaMedicamento'),
    path ('medicamentos/nuevo', login_required(CrearMedicamento), name = 'CrearMedicamento'),
    path ('medicamentos/<int:id>/actualizar',login_required(ActualizarMedicamento), name = 'ActualizarMedicamento'),
    path ('medicamentos/<int:id>/eliminar', login_required(EliminarMedicamento), name = 'EliminarMedicamento'),

    path ('usuarios', login_required(ListaUsuarioView.as_view()), name = 'ListaUsuarios'),
    path ('usuarios/nuevo', login_required(CrearUsuario), name = 'CrearUsuario'),
]