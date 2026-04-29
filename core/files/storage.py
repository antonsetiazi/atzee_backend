# core/files/storage.py

import os
import uuid
from django.conf import settings
from django.core.files.storage import default_storage
from core.tenants.models import Tenant


class FileStorageService:
    """
    Storage abstraction layer.

    This service is responsible for:
    - determining storage path
    - saving files
    - deleting files
    - resolving public URL
    """

    @staticmethod
    def safe_filename(filename: str) -> str:
        """
        Convert user filename into short unique safe filename.
        Example:
        avatar.jpg -> a81f23d9c2e14f4d9c8f.jpg
        """
        ext = os.path.splitext(filename)[1].lower()

        if not ext:
            ext = ".bin"

        return f"{uuid.uuid4().hex}{ext}"

    @staticmethod
    def build_path(*, tenant: Tenant, filename: str) -> str:
        """
        Build tenant-aware storage path.

        Example:
        uploads/<tenant_id>/<filename>
        """
        safe_name = FileStorageService.safe_filename(filename)

        return os.path.join(
            "uploads",
            str(tenant.id),
            safe_name,
        )

    @staticmethod
    def save(*, path: str, file) -> str:
        """
        Save file to storage and return final path.
        """
        return default_storage.save(path, file)

    @staticmethod
    def delete(*, path: str) -> None:
        """
        Delete file from storage.
        """
        if default_storage.exists(path):
            default_storage.delete(path)

    @staticmethod
    def get_url(*, path: str) -> str:
        """
        Resolve public URL for stored file.
        """
        return default_storage.url(path)

