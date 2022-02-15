from django.urls import path
from .views import UnidadesDeMedidaListAPIView, IndicadoresDeOfertaListAPIView



urlpatterns = [
    path('unidad_medida/', UnidadesDeMedidaListAPIView.as_view()),
    path('indicador/', IndicadoresDeOfertaListAPIView.as_view()),
]