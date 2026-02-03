from core.entities.contracts import BaseEntity
from business.products.models import Product
from django.core.exceptions import ValidationError


class ProductCreateEntity(BaseEntity):
    """
    products.create entity
    """

    key = "products.create"
    domain = "business"
    permission = "business.products.add"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        query format (from frontend):
        {
            code?: str,
            name: str,
            product_type?: "good" | "service",
            description?: str
        }
        """

        # 🔴 VALIDATE NAME
        name = (query.get("name") or "").strip()
        if not name:
            raise ValidationError("Product name is required")

        # 🔴 VALIDATE CODE (optional, unique per tenant)
        code = (query.get("code") or "").strip() or None
        if code:
            if Product.objects.filter(tenant=tenant, code=code).exists():
                raise ValidationError("Product code already exists")

        # 🔴 VALIDATE PRODUCT TYPE
        product_type = query.get("product_type") or Product.TYPE_GOOD
        if product_type not in dict(Product.PRODUCT_TYPE_CHOICES):
            raise ValidationError("Invalid product type")

        product = Product.objects.create(
            tenant=tenant,
            code=code,
            name=name,
            product_type=product_type,
            description=query.get("description"),
            created_by=user,
        )

        return {
            "id": str(product.id),
            "message": "Product created successfully",
        }
