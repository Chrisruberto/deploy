from django.db import models

# Create your models here.

class Relacion(models.Model):
    nombre = models.CharField(max_length=150)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.nombre 
    
class Marca(Relacion):
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        
class MEA(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca', on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=150, verbose_name='Nombre del Producto')
    descripcion = models.CharField(max_length=150, verbose_name='Descripcion del Producto', null=True, blank=True)
    aroma = models.CharField(max_length=150, verbose_name='Aroma', null=True, blank=True)
    color = models.CharField(max_length=150, verbose_name='Color', null=True, blank=True)
    cantidad = models.IntegerField( verbose_name='Cantidad Disponible',null=True, blank=True)
    peso_neto = models.CharField(max_length=50, verbose_name='Peso neto, ml/gr', null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio', null=True, blank=True)

    class Meta:
        verbose_name = 'MEA'
        verbose_name_plural = 'MEA'

    def __str__(self):
        return  f"{self.nombre_producto} - {self.descripcion}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre del Cliente')
    telefono = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return str(self.nombre)
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.CASCADE)              
    listado = models.ManyToManyField(MEA, verbose_name='Pedido', null=True, blank=True)
    producto = models.CharField(max_length=500,null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total',null=True, blank=True)
    pago = models.BooleanField(default=True)
    nota = models.CharField(max_length=150,null=True, blank=True)
    fecha = models.DateTimeField(auto_created=True, verbose_name='Fecha del pedido',null=True, blank=True )
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return str(self.cliente)
    
    