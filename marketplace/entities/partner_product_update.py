# marketplace/entities/partner_product_update.py

from decimal import Decimal

from core.entities.contracts import BaseEntity

from business.partners.models import Partner
from marketplace.models.catalog import MarketplaceProduct

from marketplace.enum.permissions import MarketplacePermission

def as_bool(value, default=True):
    if value is None:
        return default

    if isinstance(value, bool):
        return value

    if isinstance(value, str):
        return value.lower() in ["true", "1", "yes", "on"]

    return bool(value)

class PartnerProductUpdateEntity(BaseEntity):
    key = "partner.products.update"
    domain = "marketplace"
    permission = MarketplacePermission.PARTNER_PRODUCTS_EDIT

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:
        partner = Partner.objects.filter(
            tenant=tenant,
            core_user=user
        ).first()

        product = MarketplaceProduct.objects.filter(
            tenant=tenant,
            partner=partner,
            id=data["id"]
        ).first()

        if not product:
            raise Exception("Product not found")

        product.code = data["code"]
        product.name = data["name"]
        product.type = data["type"]
        product.category_id = data.get("category_id") or None
        product.is_active = as_bool(data.get("is_active"), True)
        product.updated_by = user
        product.save()

        listing = product.listings.first()

        if listing:
            listing.price = Decimal(str(data.get("price", 0)))
            listing.duration_minutes = data.get("duration_minutes") or None
            listing.stock = data.get("stock") or None
            listing.updated_by = user
            listing.save()

        return {
            "success": True,
            "message": "Produk berhasil diperbarui",
            "id": str(product.id),
        }