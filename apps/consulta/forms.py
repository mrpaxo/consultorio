from django import forms
from .models import Consulta , Receta , RecetaDescripcion
from apps.persona.models import Paciente


class ConsultaForm(forms.ModelForm):
    paciente = forms.ModelChoiceField( required=False,label="Paciente",queryset=Paciente.objects.filter(estado = True).order_by('id'), widget=forms.Select(attrs={'class': 'required'}))
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