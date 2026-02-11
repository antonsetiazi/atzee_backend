# core/files/entities/file_my_list.py

from core.entities.contracts import BaseEntity
from core.files.models import File


class FileMyListEntity(BaseEntity):
    """
    files.my.list entity

    List files uploaded by current user.
    """

    key = "files.my.list"
    domain = "core"
    permission = "core.files.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = File.objects.filter(
            tenant=tenant,
            is_deleted=False,
            owner=user,
        ).order_by("-created_at")

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(f.id),
                "name": f.original_name,
                "mime_type": f.mime_type,
                "size": f.size,
                "created_at": f.created_at,
            }
            for f in items
        ]

        return {
            "items": data,
            "total": total,
        }
