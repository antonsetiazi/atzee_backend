# core/files/models.py

from django.db import models
from core.models.base import TenantAwareModel
from core.users.models import User


class File(TenantAwareModel):
    """
    Core file storage entity.

    This model represents any uploaded file in the platform:
    - images
    - documents
    - pdf
    - excel
    - etc

    It is domain-agnostic and can be linked to any entity
    via related_entity + related_id.
    """

    file = models.FileField(
        upload_to="uploads/",
        help_text="Stored file path (handled by storage service)"
    )

    original_name = models.CharField(
        max_length=255,
        help_text="Original filename from user"
    )

    mime_type = models.CharField(
        max_length=100,
        help_text="Detected MIME type"
    )

    size = models.BigIntegerField(
        help_text="File size in bytes"
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="uploaded_files"
    )

    related_entity = models.CharField(
        max_length=100,
        help_text="Target entity key (e.g. products, invoices)"
    )

    related_id = models.CharField(max_length=64)

    is_public = models.BooleanField(
        default=False,
        help_text="Publicly accessible file"
    )

    class Meta:
        db_table = "core_files"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["tenant", "related_entity", "related_id"]),
        ]

    def __str__(self) -> str:
        return self.original_name
