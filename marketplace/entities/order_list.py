# marketplace/entities/order_list.py

from core.entities.contracts import BaseEntity
from marketplace.models.order import Order

from django.utils.timezone import localtime
from django.db.models import Q

from marketplace.enum.permissions import MarketplacePermission

class OrderListEntity(BaseEntity):
    key = "orders.list"
    domain = "marketplace"
    permission = MarketplacePermission.ADMIN_ORDERS_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        qs = (
            Order.objects.filter(
                tenant=tenant,
            )
            .select_related("user", "partner", "selected_partner")
        )

        # 🔍 SEARCH (order number / user / partner)
        search = query.get("search")
        if search:
            qs = qs.filter(
                Q(order_number__icontains=search) |
                Q(user__full_name__icontains=search) |
                Q(partner__name__icontains=search) |
                Q(selected_partner__name__icontains=search)
            )
        
        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("-created_at")[offset:limit]

        data = []
        for o in items:
            partner = o.partner or o.selected_partner

            data.append({
                # 🔗 identity
                "id": str(o.id),
                "order_number": o.order_number,

                # 👤 USER
                "user_name": o.user.full_name or o.user.username,
                "user_phone": o.user.phone or "-",

                # 🤝 PARTNER
                "partner_name": partner.name if partner else "-",

                # 📦 fulfillment
                "fulfillment_type": o.fulfillment_type,

                # 💰 amount
                "total_amount": float(o.total_amount),

                # 💳 payment
                "payment_status": o.payment_status,

                # 🔄 order status
                "status": o.status,

                # ⏱️ time
                "created_at": localtime(o.created_at),
            })

        return {
            "items": data,
            "total": total,
        }