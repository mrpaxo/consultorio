from django.contrib import admin 

from .models import Consulta, Receta, RecetaDescripcion
# Register your models here.
admin.site.register(Consulta)
admin.site.register(Receta)
admin.site.register(RecetaDescripcion)