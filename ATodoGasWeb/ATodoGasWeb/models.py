# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    idcategoria = models.AutoField(db_column='IDcategoria', primary_key=True)  # Field name made lowercase.
    nombrecategoria = models.CharField(db_column='nombreCategoria', unique=True, max_length=30)  # Field name made lowercase.
    descripcategoria = models.CharField(db_column='descripCategoria', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'


class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    idpersona = models.OneToOneField('Persona', models.DO_NOTHING, db_column='idpersona')

    class Meta:
        managed = False
        db_table = 'cliente'


class Detalleingreso(models.Model):
    idingreso_deta = models.AutoField(primary_key=True)
    idingreso = models.ForeignKey('Ingreso', models.DO_NOTHING, db_column='idingreso')
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto')
    cantidad = models.IntegerField()
    precio_unidad = models.FloatField()
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalleingreso'


class Detalleventa(models.Model):
    idventadet = models.AutoField(primary_key=True)
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa')
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto')
    cantidad = models.IntegerField()
    preciouni = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalleventa'


class Devolucion(models.Model):
    iddevolucion = models.AutoField(primary_key=True)
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa')
    observacion = models.CharField(max_length=250, blank=True, null=True)
    fecha_devoluvcion = models.DateField()

    class Meta:
        managed = False
        db_table = 'devolucion'


class Ingreso(models.Model):
    idingreso = models.AutoField(primary_key=True)
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor')
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario')
    fecha = models.DateField()
    total_ingreso = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingreso'


class Inventario(models.Model):
    idinventario = models.AutoField(primary_key=True)
    stock = models.IntegerField()
    stockminimo = models.IntegerField(blank=True, null=True)
    idproducto = models.OneToOneField('Producto', models.DO_NOTHING, db_column='idproducto')

    class Meta:
        managed = False
        db_table = 'inventario'


class Persona(models.Model):
    idpersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    municipio = models.CharField(max_length=30, blank=True, null=True)
    identificacion = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'persona'


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre_produc = models.CharField(max_length=50)
    codigo = models.CharField(unique=True, max_length=20)
    precioventa = models.IntegerField(blank=True, null=True)
    idcategoria = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    idpersona = models.OneToOneField(Persona, models.DO_NOTHING, db_column='idpersona')

    class Meta:
        managed = False
        db_table = 'proveedor'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='IDusuario', primary_key=True)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=50)  # Field name made lowercase.
    contrasena = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    idcliente = models.IntegerField()
    idusuario = models.IntegerField()
    totalventa = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    idfactura = models.IntegerField(blank=True, null=True)
    iva = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'
