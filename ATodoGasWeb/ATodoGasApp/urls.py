from django.urls import path
from ATodoGasApp import views

urlpatterns = [    
    path('',views.home,name= "Home"),
    path('login',views.login,name= "Login"),
    path('ventas',views.ventas,name= "Ventas"),
    path('consultas',views.consultas,name= "Consultas"),
    path('crear_cliente',views.crear_cliente,name= "Crear cliente"),
    path('index',views.index,name= "Index"),
    path('modificar_cliente/<idpersona>/',views.modificar_cliente,name= "Modificar cliente"),
    path('eliminar_cliente/<idpersona>/',views.eliminar_cliente,name= "Eliminar cliente"),
    path('borrar_producto/<idfila>/',views.borrar_producto,name= "Eliminar producto"),
    path('inventario',views.inventario,name="Inventario"),
    
]