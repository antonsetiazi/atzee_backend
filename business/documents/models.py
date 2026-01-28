from django.db import models
from shared.models import TenantAwareModel


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

    notes = models.TextField(
        blank=True,
        null=True
    )

    # Generic relation target (optional)
    source_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Source domain (e.g. SALES_ORDER, PURCHASE_ORDER)"
    )

    source_id = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="ID of source object"
    )

    class Meta:
        db_table = "business_documents"
        ordering = ["-issue_date", "-created_at"]
        indexes = [
            models.Index(fields=["tenant", "number"]),
            models.Index(fields=["tenant", "document_type"]),
            models.Index(fields=["tenant", "status"]),
        ]

    def __str__(self):
        return self.number or f"Document #{self.id}"