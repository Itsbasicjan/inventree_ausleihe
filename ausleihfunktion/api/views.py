from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from .serializers import StockLoanSerializer, PersonSerializer
from ..models import StockLoan, Person

class StockLoanViewSet(viewsets.ModelViewSet):
    queryset = StockLoan.objects.all()
    serializer_class = StockLoanSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['status', 'company', 'person', 'stock_item']
    
    @action(detail=True, methods=['post'])
    def mark_returned(self, request, pk=None):
        loan = self.get_object()
        loan.returned_date = timezone.now().date()
        loan.status = 'returned'
        loan.save()
        return Response({'status': 'loan marked as returned'})

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['company']
    search_fields = ['name', 'email']