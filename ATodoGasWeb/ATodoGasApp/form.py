from django import forms
from django.forms import ModelForm
from .models import Persona,Cliente,Detalleventa,Venta

class ClienteForm(ModelForm):
    class Meta: 
        model = Persona
        fields = ["nombre","apellido","telefono","email","direccion","municipio","identificacion"]

class VentaForm(ModelForm):
    class Meta: 
        model = Venta
        fields = ["idcliente","idusuario","totalventa","fecha","formadepago","estado","idfactura","iva"]

