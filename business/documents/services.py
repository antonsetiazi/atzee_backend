# business/documents/services.py

from typing import Optional
from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal

from business.documents.models import Document, DocumentLine
from business.documents import selectors
from core.tenants.models import Tenant
from core.users.models import User
from core.events.bus import emit_event


def _get_active_document_type(
    *,
    tenant: Tenant,
    document_type_code: str
):
    """
    Internal validators
    Validasi DocumentType
    """
    document_type = selectors.get_document_type_by_code(
        tenant=tenant,
        code=document_type_code
    )

    if not document_type:
        raise ValidationError("Invalid or inactive document type.")
    
    return document_type


def _validate_status_transition(
    *,
    document: Document,
    target_status: str
) -> None:
    """
    Enforce valid document status transitions.
    """

    if document.status == Document.STATUS_VOID:
        raise ValidationError("Void document cannot be modified.")
    
    if document.status == Document.STATUS_ISSUED and target_status == Document.STATUS_DRAFT:
        raise ValidationError("Issued document cannot be reverted to draft.")
    

@transaction.atomic
def create_document(
    *,
    tenant: Tenant,
    created_by: User,
    document_type_code: str,
    issue_date,
    reference: Optional[str] = None,
    notes: Optional[str] = None,
    source_type: Optional[str] = None,
    source_id: Optional[int] = None,
) -> Document:
    """
    Create new document in DRAFT status.
    """

    document_type = _get_active_document_type(
        tenant=tenant,
        document_type_code=document_type_code
    )

    document = Document.objects.create(
        tenant=tenant,
        document_type=document_type,
        issue_date=issue_date,
        reference=reference,
        notes=notes,
        source_type=source_type,
        source_id=source_id,
        status=Document.STATUS_DRAFT,
        created_by=created_by
    )

    return document


def _generate_document_number(
    *,
    tenant: Tenant,
    document: Document
) -> str:
    """
    Generate unique document number.
    Simple default implementaion.
    Can be replaced later by sequence engine.
    """

    today = timezone.now().strftime("%Y%m%d")

    prefix = document.document_type.code
    base = f"{prefix}/{today}"

    last_doc = (
        selectors.get_document_queryset(tenant=tenant)
        .filter(
            document_type=document.document_type,
            number__startswith=base
        )
        .order_by("-number")
        .first()
    )

    if last_doc and last_doc.number:
        try:
            last_seq = int(last_doc.number.split("/")[-1])
        except ValueError:
            last_seq = 0
    
    else:
        last_seq = 0

    next_seq = last_seq + 1

    return f"{base}/{next_seq:04d}"


@transaction.atomic
def issue_document(
    *,
    tenant: Tenant,
    document_id: int,
    issued_by: User
) -> Document:
    """
    Issue document: assign number & lock it.
    """

    document = selectors.get_document_by_id(
        tenant=tenant,
        document_id=document_id
    )

    if not document:
        raise ValidationError("Document not found.")
    
    _validate_status_transition(
        document=document,
        target_status=Document.STATUS_ISSUED
    )

    if not document.number:
        document.number = _generate_document_number(
            tenant=tenant,
            document=document
        )

    document.status = Document.STATUS_ISSUED
    document.issued_at = timezone.now()
    document.updated_by = issued_by
    document.save(update_fields=[
        "number",
        "status",
        "updated_by",
        "updated_at",
    ])

    emit_event(
        name="document.issued",
        payload={
            "tenant_id": tenant.id,
            "document_id": document.id,
            "document_type": document.document_type.code,
            "total_amount": str(document.total_amount),
            "source_entity": document.source_entity,
            "source_id": document.source_id,
        }
    )

    return document


@transaction.atomic
def void_document(
    *,
    tenant: Tenant,
    document_id: int,
    voided_by: User
) -> Document:
    """
    Void an issued document.
    """

    document = selectors.get_document_by_id(
        tenant=tenant,
        document_id=document_id
    )

    if not document:
        raise ValidationError("Document not found.")
    
    if document.status != Document.STATUS_ISSUED:
        raise ValidationError("Only issued document can be voided.")
    
    document.status = Document.STATUS_VOID
    document.updated_by = voided_by
    document.save(update_fields=[
        "status",
        "updated_by",
        "updated_at",
    ])

    return document


@transaction.atomic
def delete_document(
    *,
    tenant: Tenant,
    document_id: int,
    deleted_by: User
) -> None:
    """
    Soft delete document (only draft).
    """

    document = selectors.get_document_by_id(
        tenant=tenant,
        document_id=document_id
    )

    if not document:
        raise ValidationError("Document not found.")
    
    if document.status != Document.STATUS_DRAFT:
        raise ValidationError("Only draft document can be deleted.")
    
    document.is_deleted = True
    document.updated_by = deleted_by
    document.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])
    

def recalculate_document_amount(*, document: Document) -> None:
    """
    Recalculate subtotal & total amount.
    Allowed only when document is DRAFT.
    """

    if document.status != Document.STATUS_DRAFT:
        raise ValidationError("Cannot recalculate issued document.")

    subtotal = (
        document.lines.aggregate(
            total=Sum("amount")
        )["total"]
        or Decimal("0.0000")
    )

    document.subtotal_amount = subtotal
    document.total_amount = subtotal + document.adjustment_amount

    document.save(update_fields=[
        "subtotal_amount",
        "total_amount",
        "updated_at",
    ])


def add_document_line(
    *,
    tenant: Tenant,
    document: Document,
    label: str,
    quantity,
    unit_price,
    amount,
    meta=None,
):
    if document.is_locked():
        raise ValidationError("Issued document is immutable.")

    DocumentLine.objects.create(
        tenant=tenant,
        document=document,
        label=label,
        quantity=quantity,
        unit_price=unit_price,
        amount=amount,
        meta=meta or {},
    )

    recalculate_document_amount(document=document)
