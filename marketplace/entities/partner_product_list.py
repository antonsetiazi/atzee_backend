# marketplace/entities/partner_product_list.py

from django.db.models import Prefetch, Q
from django.utils.timezone import localtime

from business.partners.models import Partner
from core.entities.contracts import BaseEntity
from marketplace.enum.permissions import MarketplacePermission
from marketplace.models.catalog import MarketplaceProduct
from marketplace.models.listing import PartnerListing


class PartnerProductListEntity(BaseEntity):
    key = "partner.products.list"
    domain = "marketplace"
    permission = MarketplacePermission.PARTNER_PRODUCTS_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:
        # ==================================================
        # PARTNER SCOPE
        # ==================================================
        partner = Partner.objects.filter(tenant=tenant, core_user=user).first()

        if not partner:
            return {
                "items": [],
                "total": 0,
            }

        # ==================================================
        # BASE QUERY
        # ==================================================
        qs = (
            MarketplaceProduct.objects.filter(
                tenant=tenant,
                partner=partner,
            )
            .select_related("category")
            .prefetch_related(
                Prefetch(
                    "listings",
                    queryset=PartnerListing.objects.filter(
                        tenant=tenant
                    ).order_by("-created_at"),
                )
            )
        )

        # ==================================================
        # SEARCH
        # ==================================================
        search = query.get("search")
        if search:
            qs = qs.filter(
                Q(name__icontains=search) | Q(code__icontains=search)
            )

        # ==================================================
        # PAGINATION
        # ==================================================
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 1000))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("name")[offset:limit]

        # ==================================================
        # RESPONSE
        # ==================================================
        data = []

        for product in items:
            listing = (
                product.listings.all()[0]
                if product.listings.exists()
                else None
            )

            data.append(
                {
                    "id": str(product.id),
                    "code": product.code,
                    "name": product.name,
                    "type": product.type,
                    "category_name": (
                        product.category.name if product.category else "-"
                    ),
                    "price": float(listing.price) if listing else 0,
                    "duration_minutes": (
                        listing.duration_minutes if listing else None
                    ),
                    "stock": listing.stock if listing else None,
                    "listing_active": listing.is_active if listing else False,
                    "is_active": product.is_active,
                    "created_at": localtime(product.created_at),
                }
            )

        return {
            "items": data,
            "total": total,
        }
