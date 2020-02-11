"""consultorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')),
"""
from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path ('', login_required(TemplateView.as_view(template_name="index.html")),name='inicio'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
    path('admin/', admin.site.urls),
    
    path('persona/', include('apps.persona.urls')),
    path('consulta/', include('apps.consulta.urls')),
    path('cita/', include('apps.cita.urls')),
    path('grafica/', include('apps.reporte.urls')),
    path('configuracion/', include('apps.configuracion.urls')),
]
