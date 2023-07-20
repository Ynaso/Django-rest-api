from apps.products.models import Producto
from rest_framework import serializers
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        exclude = ('state','created_date', 'modified_date', 'deleted_date')


    def to_representation(self, instance):
        return {

            'id': instance.id,
            'name': instance.name,
            'description':instance.description,
            'image': instance.image if instance.image else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.CategoryProduct.description if instance.CategoryProduct is not None else '',
            #aca se esta accediendo a la descripcion del modelo relacionados a las llaves foraneas en Producto, por ejemplo measure_unit y category Product
            
        }


