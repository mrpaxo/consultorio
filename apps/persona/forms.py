from django import forms
from apps.persona.models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        exclude =('estado',)


