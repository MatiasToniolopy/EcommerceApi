from rest_framework.routers import DefaultRouter
from .product_view import ProductoViewSet
from .views import *

router = DefaultRouter()

router.register(r'producto', ProductoViewSet, basename = 'producto')
router.register(r'unidad-medida', UnidadesDeMedidaViewSet, basename = 'uinidad_medida')
router.register(r'indicador', IndicadoresDeOfertaViewSet, basename = 'indicador')
router.register(r'categoria-producto', CategoriasDeProductoViewSet, basename = 'categoria_producto')


urlpatterns = router.urls