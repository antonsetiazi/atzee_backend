# business/products/entities/product_list.py

from core.entities.contracts import BaseEntity
from business.products.models import Product


class ProductListEntity(BaseEntity):
    """
    products.list entity
    """

    key = "products.list"
    domain = "business"
    permission = "business.products.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        query format (from frontend):
        {
            page: 1,
            pageSize: 10,
            search?: str,
            filters?: {},
            sort?: {}
        }
        """

        qs = Product.objects.filter(
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

        # 🔁 SERIALIZE (explicit & stable)
        data = [
            {
                "id": str(p.id),
                "code": p.code,
                "name": p.name,
                "product_type": p.product_type,
                "description": p.description,
            }
            for p in items
        ]

        return {
            "items": data,
            "total": total,
        }
