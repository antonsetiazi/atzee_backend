# core/widget/entities/widget_detail.py

from django.utils.timezone import localtime

from core.entities.contracts import BaseEntity
from core.widgets.models import UIWidget

from core.enum.permissions import CorePermission


class WidgetDetailEntity(BaseEntity):
    key = "widgets.detail"
    domain = "core"
    permission = CorePermission.ADMIN_WIDGETS_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        widget_id = query.get("id")

        widget = UIWidget.objects.filter(
            tenant=tenant,
            id=widget_id,
            is_deleted=False,
        ).first()

        if not widget:
            raise Exception("Widget not found")

        config = widget.config or {}

        # 🔥 handle kalau config array (legacy / edge case)
        if isinstance(config, list):
            config = config[0] if config else {}

        data = {
            # 🔗 identity
            "id": str(widget.id),

            # 🎯 core fields
            "type": widget.type,
            "position": widget.position,
            "title": widget.title,

            # ⏱️ schedule
            "starts_at": format_datetime_local(widget.starts_at),
            "ends_at": format_datetime_local(widget.ends_at),

            # 🎯 targeting
            "target_roles": widget.target_roles or [],
            "target_permissions": widget.target_permissions or [],

            # 🔢 order & status
            "order": widget.order,
            "is_active": widget.is_active,
        }

        # 🔥 flatten config → dot notation (PENTING)
        for key, value in config.items():
            data[f"config.{key}"] = value

        return data
    

def format_datetime_local(dt):
    if not dt:
        return None
    return localtime(dt).strftime("%Y-%m-%dT%H:%M")