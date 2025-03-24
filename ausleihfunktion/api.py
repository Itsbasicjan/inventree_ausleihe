from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from plugin.urls import PLUGIN_BASE
from .models import StockLoan, Borrower

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ['id', 'name', 'email', 'department', 'company', 'notes']
        read_only_fields = ['id']

class StockLoanSerializer(serializers.ModelSerializer):
    borrower = BorrowerSerializer(read_only=True)
    stock_item = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = StockLoan
        fields = '__all__'
        read_only_fields = ['status']

class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = StockLoanSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return StockLoan.objects.prefetch_related('borrower', 'stock_item')

urlpatterns = [
    path(f'{PLUGIN_BASE}loans/', LoanViewSet.as_view({'get': 'list', 'post': 'create'})),
    path(f'{PLUGIN_BASE}loans/<int:pk>/', LoanViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
]