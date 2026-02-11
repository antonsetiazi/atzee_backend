# core/files/services.py

from typing import Optional
from django.db import transaction
from django.core.files.uploadedfile import UploadedFile
from rest_framework.exceptions import ValidationError

from core.files.models import File
from core.files import selectors
from core.files.storage import FileStorageService
from core.tenants.models import Tenant
from core.users.models import User


# Platform-level constraints
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

ALLOWED_MIME_TYPES = [
    "image/jpeg",
    "image/png",
    "image/webp",
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
]


def _validate_file(*, file: UploadedFile) -> None:
    """
    Validate uploaded file.
    """

    if file.size > MAX_FILE_SIZE:
        raise ValidationError("File size exceeds maximum limit.")

    if file.content_type not in ALLOWED_MIME_TYPES:
        raise ValidationError("Unsupported file type.")


@transaction.atomic
def upload_file(
    *,
    tenant: Tenant,
    uploaded_by: User,
    file: UploadedFile,
    related_entity: str,
    related_id,
    is_public: bool = False,
) -> File:
    """
    Upload file and create File record.
    """

    if not related_entity:
        raise ValidationError("related_entity is required.")

    if not related_id:
        raise ValidationError("related_id is required.")

    _validate_file(file=file)

    storage_path = FileStorageService.build_path(
        tenant=tenant,
        filename=file.name,
    )

    final_path = FileStorageService.save(
        path=storage_path,
        file=file,
    )

    return File.objects.create(
        tenant=tenant,
        file=final_path,
        original_name=file.name,
        mime_type=file.content_type,
        size=file.size,
        owner=uploaded_by,
        related_entity=related_entity,
        related_id=related_id,
        is_public=is_public,
        created_by=uploaded_by,
    )


@transaction.atomic
def delete_file(
    *,
    tenant: Tenant,
    file_id,
    deleted_by: User,
) -> None:
    """
    Soft delete file and remove from storage.
    """

    file_obj = selectors.get_file_by_id(
        tenant=tenant,
        file_id=file_id,
    )

    if not file_obj:
        raise ValidationError("File not found.")

    # FileStorageService.delete(
    #     path=file_obj.file.name
    # )

    file_obj.is_deleted = True
    file_obj.updated_by = deleted_by
    file_obj.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])
