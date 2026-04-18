# marketplace/entities/partner_product_create.py

from decimal import Decimal

from core.entities.contracts import BaseEntity

from business.partners.models import Partner
from marketplace.models.catalog import MarketplaceProduct
from marketplace.models.listing import PartnerListing

from marketplace.enum.permissions import MarketplacePermission

def as_bool(value, default=True):
    if value is None:
        return default

    if isinstance(value, bool):
        return value

    if isinstance(value, str):
        return value.lower() in ["true", "1", "yes", "on"]

    return bool(value)

class PartnerProductCreateEntity(BaseEntity):
    key = "partner.products.create"
    domain = "marketplace"
    permission = MarketplacePermission.PARTNER_PRODUCTS_CREATE

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:
        partner = Partner.objects.filter(
            tenant=tenant,
            core_user=user
        ).first()

        if not partner:
            raise Exception("Partner not found")

        product = MarketplaceProduct.objects.create(
            tenant=tenant,
            partner=partner,
            code=data["code"],
            name=data["name"],
            type=data["type"],
            category_id=data.get("category_id") or None,
            is_active=as_bool(data.get("is_active"), True),
            created_by=user,
            updated_by=user,
        )

        PartnerListing.objects.create(
            tenant=tenant,
            partner=partner,
            product=product,
            price=Decimal(str(data.get("price", 0))),
            duration_minutes=data.get("duration_minutes") or None,
            stock=data.get("stock") or None,
            is_active=True,
            created_by=user,
            updated_by=user,
        )

        return {
            "success": True,
            "message": "Produk berhasil dibuat",
            "id": str(product.id),
        }