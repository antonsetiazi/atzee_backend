# core/widgets/entities/widget_update.py

from core.entities.contracts import BaseEntity
from core.widgets import services

from core.enum.permissions import CorePermission


class WidgetUpdateEntity(BaseEntity):
    key = "widgets.update"
    domain = "core"
    permission = CorePermission.ADMIN_WIDGETS_EDIT

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:

        widget_id = data.get("id")

        if not widget_id:
            raise Exception("Widget ID is required")

        widget = services.update_widget(
            tenant=tenant,
            widget_id=widget_id,
            updated_by=user,

            # 🎯 core fields
            type=data.get("type"),
            position=data.get("position"),
            title=data.get("title"),

            # ⏱️ schedule
            starts_at=data.get("starts_at"),
            ends_at=data.get("ends_at"),

            # 🎯 targeting
            target_roles=data.get("target_roles"),
            target_permissions=data.get("target_permissions"),

            # 🔧 config (SUDAH nested)
            config=data.get("config"),

            # 🔢 order & status
            order=data.get("order"),
            is_active=data.get("is_active"),
        )

        return {
            "success": True,
            "message": "Widget berhasil diperbarui",
            "id": str(widget.id),
        }