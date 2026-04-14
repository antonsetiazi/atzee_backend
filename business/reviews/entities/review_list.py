# business/reviews/entities/review_list.py

from core.entities.contracts import BaseEntity
from business.reviews.models import Review

from django.utils.timezone import localtime
from django.db.models import Q

from business.enum.permissions import BusinessPermission

class ReviewListEntity(BaseEntity):
    key = "reviews.list"
    domain = "business"
    permission = BusinessPermission.ADMIN_REVIEWS_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        qs = (
            Review.objects.filter(
                tenant=tenant,
            )
            .select_related("user", "partner", "booking", "order")
        )

        # 🔍 SEARCH (user / partner / comment)
        search = query.get("search")
        if search:
            qs = qs.filter(
                Q(user__full_name__icontains=search) |
                Q(partner__name__icontains=search) |
                Q(comment__icontains=search)
            )

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("-created_at")[offset:limit]

        data = []
        for r in items:
            data.append({
                "id": str(r.id),

                # 👤 USER
                "user_name": r.user.full_name or r.user.username,
                "user_phone": r.user.phone or "-",

                # 🤝 PARTNER
                "partner_name": r.partner.name if r.partner else "-",

                # ⭐ RATING
                "rating": r.rating,

                # 💬 COMMENT (truncate biar rapi)
                "comment": (r.comment[:80] + "...") if r.comment and len(r.comment) > 80 else (r.comment or "-"),

                # ⏱️ TIME
                "created_at": localtime(r.created_at),
            })

        return {
            "items": data,
            "total": total,
        }