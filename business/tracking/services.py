# business/tracking/services.py

from django.db import transaction
from django.utils import timezone

from business.tracking.models import PartnerLocation
from business.tracking.models import OrderTracking

@transaction.atomic
def update_partner_location(
    *,
    tenant,
    partner,
    latitude,
    longitude,
    accuracy=None
):
    return PartnerLocation.objects.create(
        tenant=tenant,
        partner=partner,
        latitude=latitude,
        longitude=longitude,
        accuracy=accuracy
    )


@transaction.atomic
def start_order_tracking(*, tenant, order, partner):
    return OrderTracking.objects.create(
        tenant=tenant,
        order=order,
        partner=partner
    )


@transaction.atomic
def stop_order_tracking(*, tracking):
    tracking.is_active = False
    tracking.ended_at = timezone.now()
    tracking.save(update_fields=["is_active", "ended_at"])