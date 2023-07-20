from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_viewsets import ProductViewSet
from apps.products.api.views.general_views import MeasureUnitViewset, IndicatorListViewset, CategoryListViewset

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename = 'products')
router.register(r'measure-units', MeasureUnitViewset, basename = 'Measure-units')
router.register(r'Indicator', IndicatorListViewset, basename = 'Indicator')
router.register(r'category-products', CategoryListViewset, basename = 'category-products')
urlpatterns = router.urls