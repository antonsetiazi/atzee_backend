# core/files/entities/file_list.py

from core.entities.contracts import BaseEntity
from core.files.models import File
from django.conf import settings

base_url = settings.BASE_BACKEND_URL
class FileListEntity(BaseEntity):
    """
    files.list entity

    Used to list files attached to an entity.
    """

    key = "files.list"
    domain = "core"
    permission = "core.files.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        related_entity = query.get("related_entity")
        related_id = query.get("related_id")

        if not related_entity or not related_id:
            return {
                "items": [],
                "total": 0,
            }

        try:
            qs = File.objects.filter(
                tenant=tenant,
                is_deleted=False,
                related_entity=related_entity,
                related_id=related_id,
            ).select_related("owner").order_by("-created_at")
        except Exception as e:
            print(e)

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = []
        for f in items:
            # frontend bisa gabungkan BASE_URL + f.url
            # file_url = f"/api/files/{f.id}/download/"  # selalu sama

            data.append({
                "id": str(f.id),
                "name": f.original_name,
                "mime_type": f.mime_type,
                "size": f.size,
                "is_public": f.is_public,
                "created_at": f.created_at,
                "owner": f.owner.username if f.owner else None,
                "url": f"{base_url}/api/files/{f.id}/download/"
            })

        return {
            "items": data,
            "total": total,
        }
