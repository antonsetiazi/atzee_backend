from django.db import models
from decimal import Decimal
from core.models.base import TenantAwareModel


class PayrollRun(TenantAwareModel):
    """
    Payroll batch per period.
    """

    STATUS_DRAFT = "draft"
    STATUS_FINALIZED = "finalized"
    STATUS_POSTED = "posted"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_FINALIZED, "Finalized"),
        (STATUS_POSTED, "Posted to Accounting"),
    ]

    period_id = models.PositiveIntegerField(
        help_text="FK to accounting.fiscal_period.id"
    )

    run_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT
    )

    motes = models.TextField(
        blank=True,
        null=True
    )


    class Meta:
        db_table = "hr_payroll_runs"
        unique_together = (
            ("tenant", "period_id"),
        )

    def __str__(self):
        return f"Payroll {self.period_id}"
    

class PayrollItem(TenantAwareModel):
    """
    Payroll result per employee (immutable after finalize).
    """

    payroll_run = models.ForeignKey(
        PayrollRun,
        on_delete=models.CASCADE,
        related_name="items"
    )

    employee_id = models.PositiveIntegerField()

    basic_salary = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0
    )

    allowance = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0
    )

    deduction = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0
    )

    tax = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0
    )

    net_salary = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )

    class Meta:
        db_table = "hr_payroll_items"
        unique_together = (
            ("tenant", "payroll_run", "employee_id"),
        )