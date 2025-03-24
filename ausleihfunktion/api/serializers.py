from rest_framework import serializers
from .models import StockLoan, Person
from stock.models import StockItem
from company.models import Company

class StockLoanSerializer(serializers.ModelSerializer):
    stock_item = serializers.PrimaryKeyRelatedField(
        queryset=StockItem.objects.all(),
        help_text="Related stock item"
    )
    person = serializers.PrimaryKeyRelatedField(
        queryset=Person.objects.all(),
        required=False,
        allow_null=True,
        help_text="Borrowing person (optional if company is set)"
    )
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        required=False,
        allow_null=True,
        help_text="Borrowing company (optional if person is set)"
    )

    class Meta:
        model = StockLoan
        fields = [
            'pk',
            'stock_item',
            'person',
            'company',
            'start_date',
            'due_date',
            'returned_date',
            'notes',
            'status'
        ]
        read_only_fields = ['status']

    def validate(self, data):
        if not data.get('person') and not data.get('company'):
            raise serializers.ValidationError("Must specify either person or company")
        return data

    def validate_due_date(self, value):
        if value <= data.get('start_date', timezone.now().date()):
            raise serializers.ValidationError("Due date must be after start date")
        return value

class PersonSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Person
        fields = ['pk', 'name', 'email', 'company', 'notes']