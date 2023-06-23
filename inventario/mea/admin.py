from django.contrib import admin
from .models import Marca, MEA, Cliente, Pedido
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ['marca','nombre_producto', 'descripcion','aroma','color',
                    'cantidad', 'peso_neto', 'precio' ]
    list_filter = ['marca',]
    search_fields = ['nombre_producto', 'descripcion']
        
class AdminC(admin.ModelAdmin):
    list_display = ['nombre','telefono']

class AdminP(admin.ModelAdmin):
    list_display = ['cliente','producto','total','pago','nota','fecha']
    
admin.site.register(Marca)
admin.site.register(MEA,Admin)
admin.site.register(Cliente,AdminC)
admin.site.register(Pedido,AdminP)