# core/users/entities/user_list.py

from core.entities.contracts import BaseEntity
from core.users.models import User

from django.utils.timezone import localtime
from django.db.models import Q

from core.enum.permissions import CorePermission

class UserListEntity(BaseEntity):
    key = "users.list"
    domain = "core"
    permission = CorePermission.ADMIN_USERS_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        qs = User.objects.all()

        # 🔍 SEARCH (nama / username / phone / email)
        search = query.get("search")
        if search:
            qs = qs.filter(
                Q(full_name__icontains=search) |
                Q(username__icontains=search) |
                Q(phone__icontains=search) |
                Q(email__icontains=search)
            )

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("-date_joined")[offset:limit]

        data = []
        for u in items:
            data.append({
                "id": str(u.id),

                # 👤 identity
                "full_name": u.full_name or "-",
                "username": u.username,

                # 📞 contact
                "phone": u.phone or "-",
                "email": u.email or "-",

                # ✅ verification
                "is_verified": u.is_verified,
                "is_phone_verified": u.is_phone_verified,

                # 🔐 status
                "is_active": u.is_active,

                # ⏱️ time
                "date_joined": localtime(u.date_joined),
            })

        return {
            "items": data,
            "total": total,
        }