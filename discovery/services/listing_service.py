# discovery/services/listing_service.py

from discovery.selectors import marketplace as marketplace_selector
# future:
# from discovery.selectors import business as business_selector


def get_service_listings(
    *, 
    tenant, 
    search=None, 
    source="marketplace", 
    categories=None, 
    city=None,
    lat=None,
    lng=None,
    radius_km=None,
):
    """
    source:
    - marketplace
    - business (future)
    - all (future hybrid)
    """

    if source == "marketplace":
        return marketplace_selector.get_service_listings(
            tenant=tenant,
            search=search,
            categories=categories,
            city=city,
            lat=lat,
            lng=lng,
            radius_km=radius_km,
        )

    return marketplace_selector.get_service_listings(
        tenant=tenant,
        search=search,
        categories=categories,
        city=city,
        lat=lat,
        lng=lng,
        radius_km=radius_km,
    )