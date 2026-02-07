# business/documents/selectors.py

from typing import Optional
from django.db.models import QuerySet

from business.documents.models import Document, DocumentType
from core.tenants.models import Tenant


def get_document_queryset(*, tenant: Tenant) -> QuerySet[Document]:
    """
    Base queryset for documents (tenant scoped).
    """
    return Document.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_documents(*, tenant: Tenant) -> QuerySet[Document]:
    """
    Get all documents for a tenant.
    """
    return (
        get_document_queryset(tenant=tenant)
        .select_related("document_type")
        .order_by("-issue_date", "-created_at")
    )


def get_document_by_id(
    *,
    tenant: Tenant,
    document_id: int
) -> Optional[Document]:
    """
    Get single document by ID.
    """
    try:
        return get_document_queryset(tenant=tenant).select_related(
            "document_type"
        ).get(id=document_id)
    except Document.DoesNotExist:
        return None
    

def get_documents_by_type(
    *,
    tenant: Tenant,
    document_type_code: str
) -> QuerySet[Document]:
    """
    Get documents by document type code.
    """
    return (
        get_document_queryset(tenant=tenant)
        .select_related("document_type")
        .filter(document_type__code=document_type_code)
        .order_by("-issue_date", "-created_at")
    )


def get_documents_by_status(
    *,
    tenant: Tenant,
    status: str
) -> QuerySet[Document]:
    """
    Get documents by status.
    """
    return (
        get_document_queryset(tenant=tenant)
        .select_related("document_type")
        .filter(status=status)
        .order_by("-issue_date", "-created_at")
    )


def get_document_by_number(
    *,
    tenant: Tenant,
    number: str
) -> Optional[Document]:
    """
    Get document by document number.
    """
    try:
        return get_document_queryset(tenant=tenant).get(number=number)
    except Document.DoesNotExist:
        return None
    

def get_document_type_queryset(*, tenant: Tenant) -> QuerySet[DocumentType]:
    """
    Base queryset for document types.
    """
    return DocumentType.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True
    )


def get_document_types(*, tenant: Tenant) -> QuerySet[DocumentType]:
    """
    Get all active document types for tenant.
    """
    return get_document_type_queryset(tenant=tenant).order_by("name")


def get_document_type_by_code(
    *,
    tenant: Tenant,
    code: str
) -> Optional[DocumentType]:
    """
    Get document type by code.
    """
    try:
        return get_document_type_queryset(tenant=tenant).get(code=code)
    except DocumentType.DoesNotExist:
        return None