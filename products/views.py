from rest_framework import viewsets
from .serializer import UnidadesDeMedidaSerializer, IndicadoresDeOfertaSerializer, CategoriasDeProductoSerializer
from .models import UnidadesDeMedida, IndicadoresDeOferta, CategoriasDeProducto


 

class UnidadesDeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadesDeMedida.objects.all()
    serializer_class = UnidadesDeMedidaSerializer
    
  
    
class IndicadoresDeOfertaViewSet(viewsets.ModelViewSet):
    queryset = IndicadoresDeOferta.objects.all()
    serializer_class = IndicadoresDeOfertaSerializer
    
    
    
class CategoriasDeProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriasDeProducto.objects.all()
    serializer_class = CategoriasDeProductoSerializer



    
    
