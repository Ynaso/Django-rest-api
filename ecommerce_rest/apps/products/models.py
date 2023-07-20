from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords


class MeasureUnit(BaseModel):

    description = models.CharField('Descripcion', max_length=50, blank=False, null=False, unique=True)
    Historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:

        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'


    def __str__(self):

        return self.description


class CategoryProduct(BaseModel):


    description = models.CharField('Descripcion', max_length=50, unique=True, blank=False, null=False)

    Historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:

        verbose_name = 'Categoria de producto'
        verbose_name_plural = 'Categorias de producto'
    def __str__(self):
        return self.description
    


class Indicator(BaseModel):
    discount_value = models.PositiveSmallIntegerField(default = 0)
    CategoryProduct=models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name="Indicador de oferta")
    Historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    class Meta:

        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de oferta'

    def __str__(self):

        return f'oferta de la categoria {self.CategoryProduct}: {self.discoumt_value} %'
    

class Producto(BaseModel):

    name = models.CharField('Nombre de producto', max_length=150, unique=True, blank = False, null = False)
    description = models.TextField('Descripcion de Producto', blank = False, null = False)
    Historical = HistoricalRecords()
    image = models.ImageField('Imagen del producto', upload_to="producto/", blank = True, null = True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida', null = True)
    CategoryProduct=models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name="Categoria de producto", null = True)

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    class Meta:

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):

        return self.name
