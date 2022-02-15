from django.db import models

# Create your models here.
from simple_history.models import HistoricalRecords

from base.models import BaseModel




class UnidadesDeMedida(BaseModel):
    description = models.CharField('Descripcion', max_length=50, blank=True, null=False, unique=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    class meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'
        
    def __str__(self):
        return self.description
    

class CategoriasDeProducto(BaseModel):
    description = models.CharField(max_length=50, unique=True, null=False, blank=False)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    class meta:
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'
    
    def __str__(self):
        return self.description
    
class IndicadoresDeOferta(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoriasDeProducto, on_delete=models.CASCADE, verbose_name="Indicador de Ofertas")
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    class meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'
    
    def __str__(self):
        return f'Oferta de la categoria {self.category_product} : {self.descount_value}%'  
    
    
class Producto(BaseModel):
    name = models.CharField('Nombre del Producto', max_length=150, unique=True, null= False, blank= False)
    description = models.TextField('Descripcion del Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(UnidadesDeMedida, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
    category_product = models.ForeignKey(CategoriasDeProducto, on_delete=models.CASCADE, verbose_name='Categoria de Producto', null=True)
    historical = HistoricalRecords()  
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.name