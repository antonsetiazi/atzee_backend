# core/widgets/entities/widget_delete.py

from core.entities.contracts import BaseEntity
from core.widgets.models import UIWidget

from core.enum.permissions import CorePermission


class WidgetDeleteEntity(BaseEntity):
    key = "widgets.delete"
    domain = "core"
    permission = CorePermission.ADMIN_WIDGETS_DELETE

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:
        widget_id = data.get("id")

        widget = UIWidget.objects.filter(
            tenant=tenant,
            id=widget_id,
            is_deleted=False,
        ).first()

        if not widget:
            raise Exception("Widget not found")

        # 🔥 SOFT DELETE
        widget.is_deleted = True
        widget.updated_by = user
        widget.save(update_fields=["is_deleted", "updated_by", "updated_at"])

        return {
            "success": True,
            "message": "Widget berhasil dihapus",
            "id": str(widget.id),
        }