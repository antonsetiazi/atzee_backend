# discovery/services/listing_service.py

from discovery.selectors import marketplace as marketplace_selector
# future:
# from discovery.selectors import business as business_selector


def get_service_listings(*, tenant, search=None, source="marketplace"):
    """
    source:
    - marketplace
    - business (future)
    - all (future hybrid)
    """

    if source == "marketplace":
        return marketplace_selector.get_service_listings(
            tenant=tenant,
            search=search
        )

    # future extension
    # elif source == "business":
    #     return business_selector.get_service_listings(...)

    # elif source == "all":
    #     merge results

    return marketplace_selector.get_service_listings(
        tenant=tenant,
        search=search
    )