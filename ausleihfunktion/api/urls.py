from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockLoanViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'loans', StockLoanViewSet, basename='loan')
router.register(r'persons', PersonViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.StockLoanViewSet.as_view({'get': 'list'}), name='loan-list'),
]

app_name = 'stock-loans'