# accounting/models/journal.py

from django.db import models
import uuid
from core.models.base import TenantAwareModel


class Journal(TenantAwareModel):
    """
    Represent satu transaksi akuntansi (header)
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    date = models.DateField()

    description = models.TextField(blank=True)

    reference = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=50, blank=True)
    # contoh: 'sales_invoice', 'payment', 'manual'

    is_posted = models.BooleanField(default=False)
    posted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "accounting_journals"
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.reference or self.id} ({self.date})"