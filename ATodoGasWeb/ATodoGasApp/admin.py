from django.contrib import admin

from ATodoGasApp.models import *

# Register your models here.

class personaAdmin (admin.ModelAdmin):
    list_display=("nombre", "apellido", "identificacion")
    search_fields=("nombre", "apellido", "identificacion")
    
class productoAdmin (admin.ModelAdmin):
    list_display=("nombre_produc", "codigo", "idcategoria")
    search_fields=("nombre_produc", "codigo")
    list_filter=("idcategoria",)

class usuarioAdmin (admin.ModelAdmin):
    list_display=("nombreusuario", "contrasena", "cargo")
    
    
class ventaAdmin (admin.ModelAdmin):
    list_display=("idventa", "idcliente", "estado")
    search_fields=("idventa", "idcliente", "idusuario")
    date_hierarchy="fecha"
    
    
class detalleventaAdmin (admin.ModelAdmin):
    list_display=("idventa", "codigoprod")
    search_fields=("idventa", "codigoprod")

admin.site.register(Usuario, usuarioAdmin)
admin.site.register(Producto, productoAdmin)
admin.site.register(Inventario)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Venta, ventaAdmin)
admin.site.register(Detalleventa, detalleventaAdmin)
admin.site.register(Ingreso)
admin.site.register(Detalleingreso)
admin.site.register(Devolucion)
admin.site.register(Persona, personaAdmin)
admin.site.register(Categoria)