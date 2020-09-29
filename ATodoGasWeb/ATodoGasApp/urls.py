from django.urls import path
from ATodoGasApp import views

urlpatterns = [    
    path('',views.home,name= "Home"),
    path('login',views.login,name= "Login"),
    path('ventas',views.ventas,name= "Ventas"),
    path('consultas',views.consultas,name= "Consultas"),
    path('crear_cliente',views.crear_cliente,name= "Crear cliente"),
    path('index',views.index,name= "Index"),

]