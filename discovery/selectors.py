# discovery/selectors.py

from django.db.models import QuerySet, Min, Count
from business.products.models import PartnerOffering, Product
from core.tenants.models import Tenant
from core.files import selectors as file_selectors


def get_listing_queryset(*, tenant: Tenant) -> QuerySet[PartnerOffering]:
    """
    Base queryset for discovery listings.
    """

    return (
        PartnerOffering.objects
        .filter(
            tenant=tenant,
            is_active=True,
            product__is_active=True,
            product__is_deleted=False,
        )
    )


def get_product_listings(*, tenant: Tenant, search: str | None = None):
    qs = (
        get_listing_queryset(tenant=tenant)
        .select_related(
            "product", 
            "partner", 
            "partner__service_profile"
        ) 
        .filter(product__product_type="good")
    )

    if search:
        qs = qs.filter(product__name__icontains=search)

    return qs.order_by("-id")


def get_service_listings(*, tenant: Tenant, search: str | None = None):
    qs = (
        get_listing_queryset(tenant=tenant)
        .filter(product__product_type=Product.TYPE_SERVICE)
    )

    if search:
        qs = qs.filter(partner__name__icontains=search)

    # 🔥 GROUP BY PARTNER
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


def filter_listings(
    *,
    tenant: Tenant,
    product_type: str | None = None,
    search: str | None = None,
) -> QuerySet[PartnerOffering]:

    qs = get_listing_queryset(tenant=tenant)

    if product_type:
        qs = qs.filter(product__product_type=product_type)

    if search:
        qs = qs.filter(product__name__icontains=search)

    return qs


def get_service_detail(*, tenant: Tenant, partner_id: int):
    """
    Get partner + offerings for service detail page
    """

    # 1. Ambil semua offering milik partner
    offerings_qs = (
        get_listing_queryset(tenant=tenant)
        .filter(partner_id=partner_id)
        .select_related(
            "product", 
            "partner", 
            "partner__service_profile"
        ) 
    )

    if not offerings_qs.exists():
        return None

    # 2. Ambil partner dari salah satu offering
    partner = offerings_qs.first().partner

    # 3. Ambil image dari core.files
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
    }