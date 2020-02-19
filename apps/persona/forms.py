from django import forms
from apps.persona.models import Paciente


class PacienteForm(forms.ModelForm):
    fech_nac = forms.DateField(label = 'Fecha nacimiento' ,widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), required=True)
    
    class Meta:
        model = Paciente
        exclude =('estado',)


