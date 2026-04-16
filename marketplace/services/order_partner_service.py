# marketplace/services/order_partner_service.py

from django.db import transaction
from django.utils import timezone
from django.core.exceptions import ValidationError

from marketplace.models.order import Order, OrderStatus, PaymentStatus


@transaction.atomic
def mark_order_completed_by_partner(*, tenant, order_id, partner):
    order = (
        Order.objects
        .select_for_update()
        .filter(tenant=tenant, id=order_id)
        .first()
    )

    if not order:
        raise ValidationError("Order tidak ditemukan")

    # 🔒 VALIDATION
    if order.partner != partner:
        raise ValidationError("Bukan partner dari order ini")

    if order.payment_status != PaymentStatus.PAID:
        raise ValidationError("Order belum dibayar")

    if order.status != OrderStatus.ON_GOING:
        raise ValidationError("Order belum berjalan")

    # 🔥 UPDATE STATE (NO MONEY MOVEMENT)
    order.status = OrderStatus.COMPLETED_BY_PARTNER
    order.save(update_fields=["status", "updated_at"])

    return order