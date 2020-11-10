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
    productos = Producto.objects.all().order_by('idproducto')
    
    encontrado = False
    if request.method == 'POST':
        codprod = request.POST["codProd"]
        id_cliente = request.POST["id_cliente"]
        nventa = request.POST["n_venta"]
        fecha = request.POST["fecha"]
        id_factura = request.POST["id_factura"]
        forma_pago = request.POST["forma_pago"]
        iva = request.POST["iva"]
        estado = request.POST["estado"]
        data = {
                "id_cliente": id_cliente,
                "nventa": nventa,
                "fecha": fecha,
                "id_factura": id_factura,
                "forma_pago":forma_pago,
                "iva": iva,
                "estado": estado,
            }
        
        if len(codprod) is 0:
            persona = Persona.objects.all()
            existe = False
            idpersona = request.POST["id_cliente"]
            for p in persona:
                if p.identificacion == idpersona:
                    existe = True

            if existe:
                messages.success(
                request, "Este cliente se encuentra en nuestra base de datos")

                return render(request, 'ATodoGasApp/ventas.html',data)
            else:
                messages.error(
                request, "Este cliente no se encuentra en nuestra base de datos, porfavor creelo")
                return redirect(to="Crear cliente")
        else:
            for p in productos:
                if p.codigo == codprod:
                    encontrado = True
            if encontrado:
                data ["codigo_p"] = codprod
                data ["precioventa"] = Producto.objects.get(codigo=codprod).precioventa
                data ["nombre_producto"] = Producto.objects.get(codigo=codprod).nombre_produc
                return render(request, 'ATodoGasApp/ventas.html',data)
            else:
                messages.error(request, "No hay ningun producto asociado a este codigo")
                return render(request, 'ATodoGasApp/ventas.html',data)
    

    return render(request, 'ATodoGasApp/ventas.html')


def consultar_cliente(request, idpersona):
    persona = Persona.objects.all()
    existe = False
    for p in persona:
        if p.identificacion == idpersona:
            existe = True

    if existe:
        messages.success(
            request, "Este cliente se encuentra en nuestra base de datos")

        return redirect(to="Ventas")
    else:
        messages.error(
            request, "Este cliente no se encuentra en nuestra base de datos, porfavor creelo")

        return redirect(to="Crear cliente")


def consultas(request):
    return render(request, 'ATodoGasApp/consultas.html')


def crear_cliente(request):
    persona = Persona.objects.all().order_by('idpersona')
    data = {
        "form": ClienteForm(),
        "persona": persona

    }

    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()

    return render(request, 'ATodoGasApp/crear_cliente.html', data)


def modificar_cliente(request, idpersona):
    persona = Persona.objects.get(idpersona=idpersona)
    data = {
        "form": ClienteForm(instance=persona)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=persona)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se ha actualizado correctamente"
            data["form"] = formulario

    return render(request, 'ATodoGasApp/modificar_cliente.html', data)


def eliminar_cliente(request, idpersona):
    persona = Persona.objects.get(idpersona=idpersona)
    persona.delete()
    return redirect(to="Crear cliente")


def index(request):
    return render(request, 'ATodoGasApp/index.html')


def prueba(request):
    return render(request, 'ATodoGasApp/prueba.html')
