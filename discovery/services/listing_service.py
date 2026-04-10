# discovery/services/listing_service.py

from discovery.selectors import marketplace as marketplace_selector
# future:
# from discovery.selectors import business as business_selector


def get_service_listings(*, tenant, search=None, source="marketplace", categories=None,):
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
        )

    return marketplace_selector.get_service_listings(
        tenant=tenant,
        search=search,
        categories=categories,
    )