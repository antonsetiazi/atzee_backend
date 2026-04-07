# business/tracking/selectors.py

from business.tracking.models import PartnerLocation


def get_latest_partner_location(*, tenant, partner):
    return (
        PartnerLocation.objects
        .filter(tenant=tenant, partner=partner)
        .order_by("-recorded_at")
        .first()
    )