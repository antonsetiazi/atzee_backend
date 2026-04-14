# business/payment_gateway/entities/payment_gateway_list.py

from core.entities.contracts import BaseEntity
from business.payment_gateway.models import PaymentGateway

from django.utils.timezone import localtime
from django.db.models import Q

from business.enum.permissions import BusinessPermission

class PaymentGatewayListEntity(BaseEntity):
    key = "payment_gateway.list"
    domain = "business"
    permission = BusinessPermission.ADMIN_PAYMENT_GATEWAY_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        qs = PaymentGateway.objects.filter(
            tenant=tenant,
        )

        # 🔍 SEARCH (reference / external id)
        search = query.get("search")
        if search:
            qs = qs.filter(
                Q(reference_id__icontains=search) |
                Q(external_id__icontains=search) |
                Q(external_reference__icontains=search)
            )

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("-created_at")[offset:limit]

        data = []
        for p in items:
            data.append({
                "id": str(p.id),

                # 🔗 reference
                "reference_type": p.reference_type,
                "reference_id": p.reference_id,

                # 💰 amount
                "amount": float(p.amount),
                "currency": p.currency,

                # 🌐 gateway
                "provider": p.provider,
                "channel": p.channel or "-",

                # 🔑 external
                "external_id": p.external_id or "-",

                # 🔄 status
                "status": p.status,

                # ⏱️ timestamps
                "created_at": localtime(p.created_at),
                "paid_at": localtime(p.paid_at) if p.paid_at else None,
            })

        return {
            "items": data,
            "total": total,
        }