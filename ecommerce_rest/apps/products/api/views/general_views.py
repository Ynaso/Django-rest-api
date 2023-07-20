
#from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from rest_framework import viewsets
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer


class MeasureUnitViewset(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer

    
class IndicatorListViewset(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer



class CategoryListViewset(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer

