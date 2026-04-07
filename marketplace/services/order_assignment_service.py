# marketplace/services/order_assignment_service.py

from django.db import transaction
from django.core.exceptions import ValidationError

from marketplace.models.order import Order
from marketplace.models.order import OrderStatus, PaymentStatus
from business.partners.models import Partner
from business.tracking.services import start_order_tracking


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

    # 🔥 start tracking
    start_order_tracking(
        tenant=tenant,
        order=order,
        partner=partner
    )

    return order


@transaction.atomic
def reject_order(*, tenant, order_id, partner):
    order = Order.objects.filter(
        tenant=tenant,
        id=order_id
    ).first()

    if not order:
        raise ValidationError("Order tidak ditemukan")

    if order.selected_partner != partner:
        raise ValidationError("Tidak berhak reject")

    # 🔥 reset selected partner
    order.selected_partner = None
    order.status = OrderStatus.PENDING
    order.save(update_fields=["selected_partner", "status"])

    return order    