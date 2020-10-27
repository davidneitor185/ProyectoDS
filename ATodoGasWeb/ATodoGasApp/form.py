from django import forms
from django.forms import ModelForm
from .models import Persona,Cliente

class ClienteForm(ModelForm):
    class Meta: 
        model = Persona
        fields = ["nombre","apellido","telefono","email","direccion","municipio","identificacion"]