# accounting/models/period.py

from django.db import models
import uuid
from core.models.base import TenantAwareModel


class AccountingPeriod(TenantAwareModel):
    """
    Periode akuntansi (bulanan)
    """

    STATUS_CHOICES = [
        ("open", "Open"),
        ("closed", "Closed"),
        ("locked", "Locked"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=20)
    # contoh: "Jan 2026"

    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="open"
    )

    is_closed = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    class Meta:
        db_table = "accounting_periods"
        ordering = ["-start_date"]
        unique_together = ("tenant", "start_date", "end_date")

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date})"