# discovery/selectors/marketplace.py

from django.db.models import QuerySet, Min, Count
from core.tenants.models import Tenant
from marketplace.models.catalog import MarketplaceProduct
from marketplace.models.listing import PartnerListing
from core.files import selectors as file_selectors


def get_product_listings(*, tenant: Tenant, search: str | None = None):
    """
    Listing produk marketplace.
    """
    qs: QuerySet[PartnerListing] = (
        PartnerListing.objects
        .filter(
            tenant=tenant,
            is_active=True,
            product__is_active=True,
            product__type="product",
        )
        .select_related("product", "partner")
    )

    if search:
        qs = qs.filter(product__name__icontains=search)

    return qs.order_by("-id")


def get_service_listings(*, tenant: Tenant, search: str | None = None):
    """
    Listing service marketplace.
    """
    qs: QuerySet[PartnerListing] = (
        PartnerListing.objects
        .filter(
            tenant=tenant,
            is_active=True,
            product__is_active=True,
            product__type="service",
        )
        .select_related("product", "partner")
    )

    if search:
        qs = qs.filter(partner__name__icontains=search)

    # GROUP BY partner
    qs = (
        qs
        .values(
            "partner_id",
            "partner__name",
        )
        .annotate(
            starting_price=Min("price"),
            service_count=Count("id"),
        )
        .order_by("partner__name")
    )

    return qs


def get_service_detail(*, tenant: Tenant, partner_id: int):
    """
    Detail service partner.
    """
    offerings_qs = (
        PartnerListing.objects
        .filter(tenant=tenant, partner_id=partner_id, is_active=True)
        .select_related("product", "partner")
    )

    if not offerings_qs.exists():
        return None

    partner = offerings_qs.first().partner

    images_qs = file_selectors.get_files_by_relation(
        tenant=tenant,
        related_entity="partner_image",
        related_id=str(partner.id),
    ).order_by("created_at")

    service_profile = getattr(partner, "service_profile", None)

    return {
        "partner": partner,
        "offerings": offerings_qs,
        "images": images_qs,
        "service_profile": service_profile,
        "location": getattr(partner, "location", "Tidak diketahui"),
    }