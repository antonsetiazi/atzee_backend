# business/users/entities/user_list.py

from core.entities.contracts import BaseEntity
from business.users.models import BusinessUser


class UserListEntity(BaseEntity):
    """
    users.list entity
    """

    key = "users.list"
    domain = "business"
    permission = "business.users.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        Expected query format:
        {
            page: 1,
            pageSize: 10,
            search?: str,
            filters?: {},
            sort?: {}
        }
        """

        qs = BusinessUser.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        # 🔍 SEARCH
        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        # 🔁 SERIALIZE
        data = [
            {
                "id": str(u.id),
                "name": u.name,
                "email": u.email,
                "phone": u.phone,
                "organization_name": u.organization_name,
            }
            for u in items
        ]

        return {
            "items": data,
            "total": total,
        }
