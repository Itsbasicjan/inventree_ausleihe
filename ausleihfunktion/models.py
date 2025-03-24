from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from stock.models import StockItem
from company.models import Company

class Person(models.Model):
    """Represents a person who can borrow items"""
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), blank=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name=_("Company"),
        null=True,
        blank=True,
        related_name='loan_contacts'
    )
    notes = models.TextField(_("Notes"), blank=True)

    class Meta:
        verbose_name = _("Loan Contact")
        verbose_name_plural = _("Loan Contacts")
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.company.name})" if self.company else self.name

class StockLoan(models.Model):
    """Tracks loaned stock items"""
    LOAN_STATUS = (
        ('active', _("Active")),
        ('returned', _("Returned")),
        ('overdue', _("Overdue")),
    )

    stock_item = models.ForeignKey(
        StockItem,
        on_delete=models.CASCADE,
        verbose_name=_("Stock Item"),
        related_name='loans'
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name=_("Borrower"),
        null=True,
        blank=True,
        related_name='loans'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name=_("Company"),
        null=True,
        blank=True,
        related_name='loans'
    )
    start_date = models.DateField(_("Loan Date"), auto_now_add=True)
    due_date = models.DateField(_("Due Date"))
    returned_date = models.DateField(_("Returned Date"), null=True, blank=True)
    notes = models.TextField(_("Notes"), blank=True)
    status = models.CharField(
        _("Status"),
        max_length=20,
        choices=LOAN_STATUS,
        default='active'
    )

    class Meta:
        verbose_name = _("Stock Loan")
        verbose_name_plural = _("Stock Loans")
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.stock_item} loaned to {self.borrower}"

    def clean(self):
        super().clean()
        if not self.person and not self.company:
            raise ValidationError(_("Must specify either a person or company"))
        
        if self.person and self.company and self.person.company != self.company:
            raise ValidationError(_("Person's company must match loan company"))

    @property
    def borrower(self):
        return self.person or self.company

    @property
    def is_overdue(self):
        from django.utils import timezone
        return self.status == 'active' and timezone.now().date() > self.due_date

    def save(self, *args, **kwargs):
        if self.is_overdue:
            self.status = 'overdue'
        super().save(*args, **kwargs)