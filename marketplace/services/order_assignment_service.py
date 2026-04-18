# marketplace/services/order_assignment_service.py

from django.db import transaction
from django.core.exceptions import ValidationError

from business.partners.models import Partner
from business.tracking.services import start_order_tracking

from marketplace.models.order import Order, OrderStatus, PaymentStatus
from marketplace.services.order_cancellation_service import cancel_order_by_partner

from core.notifications.services import NotificationService
from core.notifications.events import ORDER_ACCEPTED

@transaction.atomic
def assign_partner_to_order(*, tenant, order_id, partner_id):
    order = Order.objects.select_for_update().filter(
        tenant=tenant,
        id=order_id
    ).first()

    if not order:
        raise ValidationError("Order tidak ditemukan")

    if order.partner:
        raise ValidationError("Order sudah memiliki partner")

    partner = Partner.objects.filter(
        tenant=tenant,
        id=partner_id
    ).first()

    if not partner:
        raise ValidationError("Partner tidak valid")

    # 🔥 assign
    order.partner = partner
    order.save(update_fields=["partner"])

    # 🔥 START TRACKING
    start_order_tracking(
        tenant=tenant,
        order=order,
        partner=partner
    )

    return order


@transaction.atomic
def accept_order(*, tenant, order_id, partner):
    try:
        order = Order.objects.select_for_update().filter(
            tenant=tenant,
            id=order_id
        ).first()

        if not order:
            raise ValidationError("Order tidak ditemukan")

        if order.partner:
            raise ValidationError("Order sudah di-assign")

        if order.selected_partner != partner:
            raise ValidationError("Bukan partner yang dipilih user")
        
        if order.payment_status != PaymentStatus.PAID:
            raise ValidationError("Order belum dibayar")

        # 🔥 assign
        order.partner = partner
        order.status = OrderStatus.ACCEPTED
        order.save(update_fields=["partner", "status"])

        # ==================================================
        # 🔔 NOTIFY CUSTOMER
        # ==================================================
        NotificationService.notify(
            user=order.user,
            tenant=tenant,
            event=ORDER_ACCEPTED,
            title="Pesanan Diterima",
            message="Partner telah menerima pesanan Anda.",
            entity_type="order",
            entity_id=str(order.id),
        )

        # 🔥 start tracking
        start_order_tracking(
            tenant=tenant,
            order=order,
            partner=partner
        )

        return order
    except Exception as e:
        print(e)

@transaction.atomic
def reject_order(*, tenant, order_id, partner, reason: str = ""):
    """
    Alias: Partner reject = Partner cancel BEFORE accept
    """

    return cancel_order_by_partner(
        tenant=tenant,
        order_id=order_id,
        partner=partner,
        reason=reason,
    )