from django import forms
from .models import Consulta , Receta , RecetaDescripcion


class ConsultaForm(forms.ModelForm):
    
    class Meta:
        model = Consulta
        exclude =['receta']


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = "__all__"

class RecetaDescripcionForm(forms.ModelForm):
    class Meta:
        model = RecetaDescripcion
        fields = "__all__"