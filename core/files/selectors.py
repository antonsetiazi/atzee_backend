# core/files/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.files.models import File
from core.tenants.models import Tenant


def get_file_queryset(*, tenant: Tenant) -> QuerySet[File]:
    """
    Base queryset for File.
    """
    return File.objects.filter(
        tenant=tenant,
        is_deleted=False,
    )


def get_files(*, tenant: Tenant) -> QuerySet[File]:
    """
    Get all files for tenant.
    """
    return get_file_queryset(tenant=tenant)


def get_file_by_id(
    *,
    tenant: Tenant,
    file_id
) -> Optional[File]:
    """
    Get single file by ID within tenant.
    """
    try:
        return get_file_queryset(
            tenant=tenant
        ).get(id=file_id)
    except File.DoesNotExist:
        return None


def get_files_by_relation(
    *,
    tenant: Tenant,
    related_entity: str,
    related_id
) -> QuerySet[File]:
    """
    Get files attached to a specific entity.
    """
    return get_file_queryset(
        tenant=tenant
    ).filter(
        related_entity=related_entity,
        related_id=related_id
    )


def get_file_by_id_no_tenant(*, file_id):
    try:
        return File.objects.filter(
            id=file_id,
            is_deleted=False,
        ).select_related("tenant").first()
    except File.DoesNotExist:
        return None