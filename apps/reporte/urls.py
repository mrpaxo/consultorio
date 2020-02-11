from django.urls import path 
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . views import HombreMujeresGrafica , ExportaUsuariosCsv , ExportaPacientesCsv
urlpatterns =[
    
    path ('grafica1', login_required(TemplateView.as_view(template_name="grafica1.html")),name='Grafica1'),
    path ('grafica1/data', login_required(HombreMujeresGrafica), name = 'Grafica1Data'),

    path ('csv_usuarios/', login_required(ExportaUsuariosCsv), name = 'UsuariosCsv'),
    path ('csv_pacientes/', login_required(ExportaPacientesCsv), name = 'PacientesCsv'),
  
]