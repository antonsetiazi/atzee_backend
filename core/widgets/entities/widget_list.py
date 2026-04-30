# core/widgets/entities/widget_list.py

from core.entities.contracts import BaseEntity
from core.widgets.models import UIWidget

from django.utils.timezone import localtime
from django.db.models import Q

from core.enum.permissions import CorePermission

class WidgetListEntity(BaseEntity):
    key = "widgets.list"
    domain = "core"
    permission = CorePermission.ADMIN_WIDGETS_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        qs = UIWidget.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        # 🔍 SEARCH (type / title / position)
        search = query.get("search")
        if search:
            qs = qs.filter(
                Q(type__icontains=search) |
                Q(title__icontains=search) |
                Q(position__icontains=search)
            )

        widget_type = query.get("type")
        if widget_type:
            qs = qs.filter(type=widget_type)

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("order", "-created_at")[offset:limit]

        data = []
        for w in items:
            data.append({
                "id": str(w.id),

                # 🎯 widget info
                "type": w.type,
                "title": w.title or "-",

                # 📍 placement
                "position": w.position,

                # 🎯 targeting (diringkas biar readable)
                "target_roles": ", ".join(w.target_roles) if w.target_roles else "-",

                # ⏱️ schedule
                "starts_at": format_datetime_local(w.starts_at),
                "ends_at": format_datetime_local(w.ends_at),

                # 🔐 status
                "is_active": w.is_active,

                # 🔢 order
                "order": w.order,
            })

        return {
            "items": data,
            "total": total,
        }
    

def format_datetime_local(dt):
    if not dt:
        return None
    return localtime(dt).strftime("%Y-%m-%dT%H:%M")