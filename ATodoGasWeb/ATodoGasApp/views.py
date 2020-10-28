from django.shortcuts import render,HttpResponse
from .form import ClienteForm
from .models import *

# Create your views here.
def login(request):
    return render(request, 'registration/login.html')

def home(request):
    return render(request, 'ATodoGasApp/home.html')

def ventas(request):

    return render(request, 'ATodoGasApp/ventas.html')

def consultas(request):
    return render(request, 'ATodoGasApp/consultas.html')

def crear_cliente(request):
    data = {
        "form":ClienteForm()

    }
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            identifiacion = formulario.cleaned_data['identifiacion']
            persona = Persona.objects.filter(identifiacion__icontains=identifiacion)
            if (persona):
                cliente = Cliente(idpersona=persona.idpersona)
                cliente.save()
                
            else:
                formulario.save()
                persona = Persona.objects.filter(identifiacion__icontains=identifiacion)
                cliente = Cliente(idpersona=persona.idpersona)
                cliente.save()
        
            
    return render(request, 'ATodoGasApp/crear_cliente.html',data)

def index(request):
    return render(request, 'ATodoGasApp/index.html')
    



