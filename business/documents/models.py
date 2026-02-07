# business/documents/models.py

from django.db import models
from core.models.base import TenantAwareModel
from decimal import Decimal


class DocumentType(TenantAwareModel):
    """
    Document type configuration.
    Example: INVOICE, RECEIPT, DELIVERY_ORDER
    """

    code = models.CharField(
        max_length=50,
        help_text="Unique document type code (e.g. INVOICE, RECEIPT)"
    )

    name = models.CharField(
        max_length=100,
        help_text="Human readable name"
    )

    description = models.TextField(
        blank=True,
        null=True
    )


    class Meta:
        db_table = "business_document_types"
        unique_together = ("tenant", "code")
        ordering = ["name"]

    def __str__(self):
        return f"{self.code} - {self.name}"
    

class Document(TenantAwareModel):
    """
    Core business document.
    Generic representation for invoice, receipt, delivery order, etc.
    """

    STATUS_DRAFT = "draft"
    STATUS_ISSUED = "issued"
    STATUS_CANCELLED = "cancelled"
    STATUS_VOID = "void"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_ISSUED, "Issued"),
        (STATUS_VOID, "Void"),
    ]

    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.PROTECT,
        related_name="documents"
    )

    number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Generated document number"
    )

    reference = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="External or manual reference"
    )

    status =  models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT
    )

    issue_date = models.DateField(
        help_text="Date when document is issued"
    )

    issued_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Timestamp when document is legally issued"
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    # Generic relation target (optional)
    source_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Source domain (e.g. SALES_ORDER, PURCHASE_ORDER)"
    )

    source_id = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )

    subtotal_amount = models.DecimalField(
        max_digits=18,
        decimal_places=4,
        default=0
    )

    adjustment_amount = models.DecimalField(
        max_digits=18,
        decimal_places=4,
        default=0,
        help_text="Discount, rounding, etc"
    )

    total_amount = models.DecimalField(
        max_digits=18,
        decimal_places=4,
        default=0
    )

    class Meta:
        db_table = "business_documents"
        ordering = ["-issue_date", "-created_at"]
        indexes = [
            models.Index(fields=["tenant", "number"]),
            models.Index(fields=["tenant", "document_type"]),
            models.Index(fields=["tenant", "status"]),
        ]

    def is_locked(self) -> bool:
        return self.status in [
            self.STATUS_ISSUED,
            self.STATUS_VOID,
        ]

    def __str__(self):
        return self.number or f"Document #{self.id}"
    

class DocumentLine(TenantAwareModel):
    """
    Generic document line.
    Does NOT know product, tax, or accounting.
    """

    document = models.ForeignKey(
        "Document",
        on_delete=models.CASCADE,
        related_name="lines"
    )

    label = models.CharField(
        max_length=255,
        help_text="Human readable line description"
    )

    quantity = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        default=Decimal("1.0000")
    )

    unit_price = models.DecimalField(
        max_digits=16,
        decimal_places=4
    )

    amount = models.DecimalField(
        max_digits=18,
        decimal_places=4,
        help_text="quantity × unit_price (stored, not computed)"
    )

    meta = models.JSONField(
        default=dict,
        blank=True,
        help_text="Optional metadata (e.g. product_id, service_ref)"
    )

    class Meta:
        db_table = "business_document_lines"
        ordering = ["id"]    