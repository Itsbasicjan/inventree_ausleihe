from django.contrib import admin
from .models import StockLoan, Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
    search_fields = ('name', 'email', 'company__name')
    list_filter = ('company',)
    autocomplete_fields = ('company',)

@admin.register(StockLoan)
class StockLoanAdmin(admin.ModelAdmin):
    list_display = ('stock_item', 'borrower', 'start_date', 'due_date', 'status')
    list_filter = ('status', 'company', 'start_date')
    search_fields = (
        'stock_item__part__name',
        'person__name',
        'company__name',
        'notes'
    )
    autocomplete_fields = ('stock_item', 'person', 'company')
    date_hierarchy = 'start_date'
    fieldsets = (
        (None, {
            'fields': ('stock_item', ('person', 'company'))
        }),
        ('Dates', {
            'fields': ('start_date', 'due_date', 'returned_date')
        }),
        ('Status', {
            'fields': ('status', 'notes')
        }),
    )

    def borrower(self, obj):
        return obj.borrower
    borrower.short_description = _("Borrower")