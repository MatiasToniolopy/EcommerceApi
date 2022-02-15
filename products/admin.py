from django.contrib import admin
from products.models import *

class UnidadesDeMedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    
class CategoriasDeProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(UnidadesDeMedida, UnidadesDeMedidaAdmin)
admin.site.register(CategoriasDeProducto, CategoriasDeProductoAdmin)
admin.site.register(IndicadoresDeOferta)
admin.site.register(Producto)