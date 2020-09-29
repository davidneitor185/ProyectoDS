from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    return render(request, 'ATodoGasApp/login.html')

def home(request):
    return render(request, 'ATodoGasApp/home.html')

def ventas(request):
    return render(request, 'ATodoGasApp/ventas.html')

def consultas(request):
    return render(request, 'ATodoGasApp/consultas.html')

def crear_cliente(request):
    return render(request, 'ATodoGasApp/crear_cliente.html')

