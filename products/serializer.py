from .models import UnidadesDeMedida, CategoriasDeProducto, IndicadoresDeOferta
from rest_framework import serializers

class UnidadesDeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadesDeMedida
        exclude = ('state', 'created_date', 'modified_date', 'delete_date')

class CategoriasDeProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasDeProducto
        exclude = ('state','created_date', 'modified_date', 'delete_date')
        
class IndicadoresDeOfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicadoresDeOferta
        exclude = ('state','created_date', 'modified_date', 'delete_date')


