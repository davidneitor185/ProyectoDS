from django.shortcuts import render, HttpResponse, redirect
from .form import ClienteForm
from .models import *
from django.contrib import messages

# Create your views here.


def login(request):
    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'ATodoGasApp/home.html')


def ventas(request):
   
    return render(request, 'ATodoGasApp/ventas.html')

def consultar_cliente(request, idpersona):
    #persona = Persona.objects.all()
    #existe=False
    #for p in persona:
     #   if p.identificacion == idpersona:
     #       existe=True

    #if existe:
     #   messages.success(request,idpersona)
    #    return redirect(to= "Ventas")
    #else:
        #messages.success(request,p.identificacion)
    messages.success(request,idpersona)     
    return redirect(to="Crear cliente")

def consultas(request):
    return render(request, 'ATodoGasApp/consultas.html')


def crear_cliente(request):
    persona = Persona.objects.all().order_by('idpersona')
    data = {
        "form":ClienteForm(),
        "persona": persona

    }


    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()


    return render(request, 'ATodoGasApp/crear_cliente.html',data)

def modificar_cliente(request, idpersona):
    persona= Persona.objects.get(idpersona=idpersona)
    data = {
        "form":ClienteForm(instance=persona)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data= request.POST, instance=persona)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se ha actualizado correctamente"
            data["form"] = formulario

    return render(request, 'ATodoGasApp/modificar_cliente.html', data )

def eliminar_cliente(request, idpersona):
    persona= Persona.objects.get(idpersona=idpersona)
    persona.delete()
    return redirect(to="Crear cliente")


def index(request):
    return render(request, 'ATodoGasApp/index.html')

def prueba(request):
    return render(request, 'ATodoGasApp/prueba.html')
