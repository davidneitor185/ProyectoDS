from django.shortcuts import render, HttpResponse, redirect
from .form import ClienteForm
from .models import *
from django.contrib import messages

# Create your views here.
class Rowventas:
    def __init__(self):
        self.id =0
        self.codigo = 0
        self.cantidad = 0
        self.nombreprod = ""
        self.precio = 0
        self.total = 0


def login(request):
    rowsventas.clear()
    return render(request, 'registration/login.html')


def home(request):
    rowsventas.clear()
    return render(request, 'ATodoGasApp/home.html')

rowsventas= list()



def ventas(request):
    
    productos = Producto.objects.all().order_by('idproducto')
    encontrado = False
    persona = Persona.objects.all()
    existe = False
    
    if request.method == 'POST':
        print("holi")
        
        id_cliente = request.POST["id_cliente"]
        nventa = request.POST["n_venta"]
        fecha = request.POST["fecha"]
        id_factura = request.POST["id_factura"]
        forma_pago = request.POST["forma_pago"]
        iva = request.POST["iva"]
        estado = request.POST["estado"]
        codprod = request.POST["codProd"]
        cantidad = request.POST["cantidad"]
        precio_venta = request.POST["precio_venta"]
        descuento = request.POST["descuento"]

        

        
        data = {
                "id_cliente": id_cliente,
                "nventa": nventa,
                "fecha": fecha,
                "id_factura": id_factura,
                "forma_pago":forma_pago,
                "iva": iva,
                "estado": estado,
                "codProd":codprod,
                "cantidad":cantidad,
                "precio_venta":precio_venta,
                "descuento" : descuento,
                "tabla_cont": rowsventas
            }
        
        
        if 'consultar_cliente' in request.POST:
            print("consultar cliente")  
            
            
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
        elif 'consultar_producto' in request.POST:
            print("consultar producto")
             
            for p in productos:
                if p.codigo == codprod:
                    encontrado = True
                    
            if encontrado:
                
                data ["precio_venta"] = Producto.objects.get(codigo=codprod).precioventa
                data ["nombre_producto"] = Producto.objects.get(codigo=codprod).nombre_produc
                
                
                return render(request, 'ATodoGasApp/ventas.html',data)
            else:
                data ["codProd"] = None
                data ["precio_venta"] = None
                data ["cantidad"] = None
                data ["descuento"] = None
                messages.error(request, "No hay ningun producto asociado a este codigo")
                return render(request, 'ATodoGasApp/ventas.html',data)
        elif 'agregar' in request.POST:
                
            codigo = request.POST["codProd"]
            nombre = Producto.objects.get(codigo=codigo).nombre_produc
            cantidad = int(request.POST["cantidad"])
            precio = Producto.objects.get(codigo=codigo).precioventa - int(request.POST["descuento"])
            total = cantidad * precio

            row = Rowventas()
            row.id= len(rowsventas)
            row.codigo = codigo
            row.nombreprod = nombre
            row.cantidad = cantidad
            row.precio = precio
            row.total = total

            

            rowsventas.append(row)
            data["tabla_cont"] = rowsventas
            return render(request, 'ATodoGasApp/ventas.html', data)
        elif 'borrar' in request.POST:
            

            id_row =int( request.POST["id_row"])
            print(id_row)
            #print(rowsventas[0].id)           
            #rowsventas.pop(id_row)
            #i=0
            #for r in rowsventas:
            #    if r.codigo ==codigo_row:
            #        rowsventas.remove(i)
            #    else: i+=1
            #if len(rowsventas) != 0:
            #    for i in range(len(rowsventas)):
            #        rowsventas[i].id = i
            #data["tabla_cont"] = rowsventas
            return render(request, 'ATodoGasApp/ventas.html', data)


            


            


    

    return render(request, 'ATodoGasApp/ventas.html')


def consultar_cliente(request, idpersona):
    rowsventas.clear()
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
    rowsventas.clear()
    return render(request, 'ATodoGasApp/consultas.html')


def crear_cliente(request):
    rowsventas.clear()
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
    rowsventas.clear()
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
    rowsventas.clear()
    persona = Persona.objects.get(idpersona=idpersona)
    persona.delete()
    return redirect(to="Crear cliente")


def index(request):
    return render(request, 'ATodoGasApp/index.html')


def prueba(request):
    return render(request, 'ATodoGasApp/prueba.html')
