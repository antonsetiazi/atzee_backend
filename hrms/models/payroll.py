# hrms/models/payroll.py

from django.db import models

from core.models.base import TenantAwareModel
from hrms.enums import PayrollStatus
from hrms.models.employee import Employee


class Payroll(TenantAwareModel):
    """
    Employee payroll record.
    """

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="payrolls"
    )

    payroll_period = models.CharField(max_length=20)

    basic_salary = models.DecimalField(
        max_digits=18, decimal_places=2, default=0
    )

    allowance_amount = models.DecimalField(
        max_digits=18, decimal_places=2, default=0
    )

    deduction_amount = models.DecimalField(
        max_digits=18, decimal_places=2, default=0
    )

    net_salary = models.DecimalField(
        max_digits=18, decimal_places=2, default=0
    )

    status = models.CharField(
        max_length=30,
        choices=PayrollStatus.choices,
        default=PayrollStatus.DRAFT,
    )

    processed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "hrms_payrolls"
        ordering = ["-created_at"]
        unique_together = ("tenant", "employee", "payroll_period")

    def __str__(self):
        return f"{self.employee} - {self.payroll_period}"
