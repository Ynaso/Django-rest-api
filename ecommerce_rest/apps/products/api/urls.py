from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicatorListAPIView, CategoryListAPIView
from apps.products.api.views.product_viewsets import productListCreateAPIView,ProductRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = "MeasureUnits"),
    path('Indicator/', IndicatorListAPIView.as_view(), name = "MeasureUnits"),
    path('Category/', CategoryListAPIView.as_view(), name = "MeasureUnits"),
]

