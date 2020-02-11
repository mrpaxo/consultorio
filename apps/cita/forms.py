from django import forms
from apps.cita.models import Cita

COLOR = (
    ('#fcf12e','Amarillo'),
    ('#ff0000','Rojo'),
    ('#5fb5f3','Azul'),
    ('#51ee4d','Verde'),
    
    
)
STATUS =((1,'Activo'),
(2,'Cancelado'),
(3,'No Asistio'),)

class CitaForm(forms.ModelForm):
    inicio = forms.DateTimeField(widget=forms.DateTimeInput(format = '%d-%m-%Y %H:%M',attrs={'readonly': True}), input_formats=('%d-%m-%Y %H:%M',), required=True)
    color = forms.ChoiceField(choices = COLOR,widget=forms.Select())
    status = forms.ChoiceField(choices = STATUS,widget=forms.Select())
    class Meta:
        model = Cita
        #fields ="__all__"
        fields = ["paciente",
                  "inicio",
                  "color",
                  "observacion",
                  "status"]


