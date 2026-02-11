# core/classifications/tags/entities/tag_detach.py

from django.contrib.contenttypes.models import ContentType
from core.entities.contracts import BaseEntity
from core.classifications.tags.models import TagRelation


class TagDetachEntity(BaseEntity):
    key = "tags.detach"
    domain = "core"
    permission = "core.tags.update"

    # 🔹 WAJIB: implementasi query() meski tidak digunakan
    def query(self, *, user, tenant, query: dict) -> dict:
        return {"items": [], "total": 0}

    # 🔹 Hanya execute yang digunakan untuk detach
    def execute(self, *, user, tenant, data: dict) -> dict:
        tag_id = data.get("tag_id")
        model = data.get("model")
        object_id = data.get("object_id")

        if not tag_id or not model or not object_id:
            return {"success": False}

        app_label, model_name = model.split(".")

        content_type = ContentType.objects.get(
            app_label=app_label,
            model=model_name,
        )

        TagRelation.objects.filter(
            tenant=tenant,
            tag_id=tag_id,
            content_type=content_type,
            object_id=object_id,
        ).delete()

        return {"success": True}
