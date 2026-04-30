# core/widgets/entities/widget_create.py

from core.entities.contracts import BaseEntity
from core.widgets import services

from core.enum.permissions import CorePermission


class WidgetCreateEntity(BaseEntity):
    key = "widgets.create"
    domain = "core"
    permission = CorePermission.ADMIN_WIDGETS_CREATE

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:

        widget = services.create_widget(
            tenant=tenant,
            created_by=user,

            # 🎯 core fields
            type=data.get("type"),
            position=data.get("position"),
            title=data.get("title"),

            # ⏱️ schedule
            starts_at=data.get("starts_at"),
            ends_at=data.get("ends_at"),

            # 🎯 targeting
            target_roles=data.get("target_roles", []),
            target_permissions=data.get("target_permissions", []),

            # 🔧 config
            config=data.get("config", {}),

            # 🔢 order & status
            order=data.get("order", 50),
            is_active=data.get("is_active", True),
        )

        return {
            "success": True,
            "message": "Widget berhasil dibuat",
            "id": str(widget.id),
        }