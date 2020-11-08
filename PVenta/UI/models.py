from django.db import models

# Create your models here.

class Cliente(models.Model):
    idCliente = models.BigIntegerField(db_column='idCliente', primary_key=True, null=False, blank=True)  # Field name made lowercase.
    idTipo = models.ForeignKey('TipoCliente',models.DO_NOTHING,db_column='idTipo', blank=True, null=False)  # Field name made lowercase.
    nameCl = models.CharField(db_column='nameCl', max_length=30, blank=True, null=False)  # Field name made lowercase.
    apellidoP = models.CharField(db_column ='apellidoP',max_length=30, blank=True, null=False)  # Field name made lowercase.
    apellidoM = models.CharField(db_column ='apellidoM',max_length=30, blank=True, null=False)  # Field name made lowercase.
    calle = models.CharField(db_column='calle', max_length=30, blank=True, null=False)  # Field name made lowercase.
    numero = models.IntegerField(db_column ='numero', blank=True, null=False)  # Field name made lowercase.
    colonia = models.CharField(db_column='colonia',max_length=30, blank=True, null=False)  # Field name made lowercase.
    email = models.EmailField(db_column='email',max_length=50, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='celular',max_length = 10, blank=True, null=False)  # Field name made lowercase.
    puntos = models.IntegerField(db_column='puntos', blank=True, null=False)  # Field name made lowercase.
    def __str__(Cliente):
        return str('('+str(Cliente.idCliente)+')' +' '+Cliente.nameCl)
    class Meta:
        managed = False
        db_table = 'Cliente'
class Articulo(models.Model):
    idAr = models.BigIntegerField(db_column='idAr', primary_key=True, null=False)  
    nameAr = models.CharField(db_column='nameAr', max_length=30, blank=True, null=False)  
    idcat = models.ForeignKey('Categoria',models.DO_NOTHING,db_column='idcat',  blank=True)  # Field name made lowercase.
    talla = models.CharField(db_column='talla',max_length=1, blank=True, null=False)  
    cantidad = models.IntegerField(db_column='cantidad', blank=True, null=False)  
    precio = models.FloatField(db_column='precio', blank=True, null=False)  
    descripcion = models.CharField(db_column='descripcion',max_length=100, blank=True, null=True) 
    def __str__(Articulo):
        return str('('+str(Articulo.idAr)+')' +' '+Articulo.nameAr) 
    class Meta:
        managed = False
        db_table = 'Articulo'

class Categoria(models.Model):
    idcat = models.BigIntegerField(db_column='idcat', primary_key=True)
    Nombre = models.CharField(db_column='namecat', max_length=30, null=False)
    def __str__(Categoria):
        return str('('+str(Categoria.idcat)+')' +' '+Categoria.Nombre)
    class Meta:
        managed = False
        db_table = 'Categoria'
class Apartar(models.Model):
    idApartar = models.BigIntegerField(db_column='idApartar', primary_key=True, null=False, blank=True)
    idAr = models.ForeignKey('Articulo',models.DO_NOTHING,db_column='idAr', blank=True, null=False)
    idCliente = models.ForeignKey('Cliente',models.DO_NOTHING,db_column='idCliente' ,blank=True, null=False)  # Field name made lowercase.
    diaApartar = models.IntegerField(db_column='diaApartar', blank=True, null=False)
    mesApartar = models.IntegerField(db_column='mesApartar', blank=True, null=False)
    anioApartar = models.IntegerField(db_column='anioApartar', blank=True, null=False)
    class Meta:
        managed = False
        db_table = 'Apartar'

class Venta(models.Model):
    idVenta = models.BigIntegerField(db_column='idVenta', primary_key=True, null=False, blank=True)
    idCliente = models.ForeignKey('Cliente',models.DO_NOTHING,db_column='idCliente' , blank=True, null=False)  # Field name made lowercase.
    total = models.FloatField(db_column='total', blank=True, null=False)
    class Meta:
        managed = False
        db_table = 'Venta'

class DetalleVenta(models.Model):
    #idDetalleVenta = models.BigAutoField(db_column='idDetalleVenta', primary_key=True, null=False, blank=True)
    idVenta = models.ForeignKey('Venta',models.DO_NOTHING,db_column='idVenta' , blank=True, null=False)
    idAr = models.ForeignKey('Articulo',models.DO_NOTHING,db_column='idAr' , blank=True, null=False)
    cantidadA = models.IntegerField(db_column='cantidadA', blank=True, null=False)
    class Meta:
        managed = False
        db_table = 'DetalleVenta'
class TipoCliente(models.Model):
    idTipo = models.BigIntegerField(db_column='idTipo', primary_key=True, null=False)
    nameTipo = models.CharField(db_column='nameTipo', max_length=30, blank=True, null=False)
    puntosT = models.IntegerField(db_column='puntosT', blank=True, null=False)
    def __str__(TipoCliente):
        return str('('+str(TipoCliente.idTipo)+')' +' '+TipoCliente.nameTipo)
    class Meta:
        managed = False
        db_table = 'TipoCliente'
class Abono(models.Model):
    idAbono = models.BigIntegerField(db_column='idAbono', primary_key=True, null=False)
    idCliente = models.ForeignKey('Cliente',models.DO_NOTHING,db_column='idCliente' , blank=True, null=False)  # Field name made lowercase.
    idVenta = models.ForeignKey('Venta',models.DO_NOTHING,db_column='idVenta' , blank=True, null=False)
    monto = models.FloatField(db_column='monto', blank=True, null=False)
    class Meta:
        managed = False
        db_table = 'Abono'

