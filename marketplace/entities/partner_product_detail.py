# marketplace/entities/partner_product_detail.py

from core.entities.contracts import BaseEntity

from business.partners.models import Partner
from marketplace.models.catalog import MarketplaceProduct

from marketplace.enum.permissions import MarketplacePermission


class PartnerProductDetailEntity(BaseEntity):
    key = "partner.products.detail"
    domain = "marketplace"
    permission = MarketplacePermission.PARTNER_PRODUCTS_EDIT

    def query(self, *, user, tenant, query: dict) -> dict:
        partner = Partner.objects.filter(
            tenant=tenant,
            core_user=user
        ).first()

        product_id = query.get("id")

        product = MarketplaceProduct.objects.filter(
            tenant=tenant,
            partner=partner,
            id=product_id
        ).first()

        if not product:
            raise Exception("Product not found")

        listing = product.listings.first()

        return {
            "id": str(product.id),
            "code": product.code,
            "name": product.name,
            "type": product.type,
            "category_id": str(product.category_id) if product.category_id else "",
            "price": float(listing.price) if listing else 0,
            "duration_minutes": listing.duration_minutes if listing else "",
            "stock": listing.stock if listing else "",
            "is_active": product.is_active,
        }