# discovery/selectors/marketplace.py

from django.db.models import F, Value, DecimalField, IntegerField
from django.db.models.functions import Coalesce
from decimal import Decimal
from django.db.models import QuerySet, Min, Count
from django.db.models.expressions import RawSQL
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


def get_service_listings(
        *, 
        tenant: Tenant, 
        search: str | None = None, 
        categories: list[str] | None = None,
        city: str | None = None,
        lat: float | None = None,
        lng: float | None = None,
        radius_km: int | None = None,
):
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
        .select_related("product", "partner", "product__category")
    )

    if search:
        qs = qs.filter(partner__name__icontains=search)

    if categories:
        qs = qs.filter(
            product__category__code__in=categories
        )
        
    # 🏙 CITY FILTER (ONLY IF NOT USING GEO)
    if city and not lat and not lng:
        qs = qs.filter(partner__city__code=city)


    # GROUP BY partner
    qs = (
        qs
        .values(
            "partner_id",
            "partner__name",
            "partner__city__name", 
            "partner__search_latitude",
            "partner__search_longitude",
        )
        .annotate(
            starting_price=Min("price"),
            service_count=Count("id"),
            rating=Coalesce(
                F("partner__rating_avg"),
                Value(Decimal("0.0")),
                output_field=DecimalField(max_digits=4, decimal_places=2),
            ),

            rating_count=Coalesce(
                F("partner__rating_count"),
                Value(0),
                output_field=IntegerField(),
            ),
        )
    )

    # =========================
    # 🔥 ALWAYS RETURN LIST
    # =========================
    data = list(qs)


    # =========================
    # 🌍 GEO SORT (OPTIONAL)
    # =========================
    if lat and lng:
        from math import radians, sin, cos, sqrt, atan2

        def haversine(lat1, lon1, lat2, lon2):
            R = 6371
            dlat = radians(lat2 - lat1)
            dlon = radians(lon2 - lon1)

            a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
            c = 2 * atan2(sqrt(a), sqrt(1-a))

            return R * c

        for item in data:
            plat = item.get("partner__search_latitude")
            plng = item.get("partner__search_longitude")

            if plat is not None and plng is not None:
                item["distance"] = haversine(lat, lng, plat, plng)
            else:
                item["distance"] = 9999

        # 🔥 SORT BY DISTANCE
        data.sort(key=lambda x: x["distance"])

        # 🔥 RADIUS FILTER
        if radius_km:
            data = [d for d in data if d["distance"] <= radius_km]

    return data


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