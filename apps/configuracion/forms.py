from django import forms
from apps.configuracion.models import Enfermedad , Medicamento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EnfermedadForm(forms.ModelForm):
    
    class Meta:
        model = Enfermedad
        fields = "__all__"



class MedicamentoForm(forms.ModelForm):
    
    class Meta:
        model = Medicamento
        fields = "__all__"

class UsuarioForm(UserCreationForm):
    username = forms.CharField(label ='Usuario',max_length=30, required=True)
    password1 = forms.CharField(label ='Contraseña',max_length=30, required=True,widget=forms.TextInput(attrs={'type': 'password'}))
    password2 = forms.CharField(label ='Confirme Contraseña',max_length=30, required=True,widget=forms.TextInput(attrs={'type': 'password'}))
    first_name = forms.CharField(label ='Nombre',max_length=30, required=True)
    last_name = forms.CharField(label ='Apellidos', max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Requiere un email valido')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )