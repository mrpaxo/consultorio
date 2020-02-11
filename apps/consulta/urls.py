from django.urls import path 
from apps.consulta.views import ListaConsultaView , CrearConsulta , ActualizarConsulta , EliminarConsulta ,ActualizarReceta,CrearReceta, CrearRecetaDescripcion , EliminarRecetaDescripcion , ConsultaDetailView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
urlpatterns =[
    path ('consultas', login_required(ListaConsultaView.as_view()), name = 'ListaConsulta'),
    path ('consultas/nuevo', login_required(CrearConsulta), name = 'CrearConsulta'),
    path ('consultas/<int:id>/actualizar', login_required(ActualizarConsulta), name = 'ActualizarConsulta'),
    path ('consultas/<int:id>/eliminar', login_required(EliminarConsulta), name = 'EliminarConsulta'),
    #path ('receta', TemplateView.as_view(template_name="receta/receta.html")),
    path ('receta/<int:id>/nuevo', login_required(CrearReceta), name = 'CrearReceta'),
    path ('receta/<int:id>/actualizar', login_required(ActualizarReceta), name = 'ActualizarReceta'),
    path ('receta_descripcion/nuevo', login_required(CrearRecetaDescripcion), name = 'CrearRecetaDescripcion'),
    path ('receta_descripcion/<int:id>/eliminar', login_required(EliminarRecetaDescripcion), name = 'EliminarRecetaDescripcion'),
    path ('receta_descripcion/<int:pk>/imprime', login_required(ConsultaDetailView.as_view()), name = 'ConsultaDetailView'),
]