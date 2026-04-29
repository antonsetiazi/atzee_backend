# marketplace/serializers/order_serializer.py

from decimal import Decimal
from rest_framework import serializers
from django.db import transaction
import uuid
from math import radians, sin, cos, sqrt, atan2

from core.account.selectors import get_user_address_by_id
from business.partners.selectors import get_partner_by_id

from marketplace.models.order import Order, OrderItem
from marketplace.models.order import PaymentStatus, OrderStatus
from marketplace.models.listing import PartnerListing

from core.fees.services.fee_engine import FeeEngine
from core.fees.types import FeeInput
from core.fees.models import OrderFee


def calculate_distance_km(lat1, lon1, lat2, lon2):
    """
    Haversine formula
    """
    r = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return r * c


def calculate_transport_fee(distance_km):
    """
    Rules:
    0-3 km gratis
    selebihnya Rp2.500/km
    """
    free_km = 3
    per_km = Decimal("2500")

    if distance_km <= free_km:
        return Decimal("0")

    extra = Decimal(str(distance_km - free_km))
    return extra * per_km


class OrderItemInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    qty = serializers.IntegerField(min_value=1)


class CreateOrderSerializer(serializers.Serializer):
    items = OrderItemInputSerializer(many=True)
    booking_id = serializers.IntegerField(required=False, allow_null=True)

    # 🔥 NEW
    address_id = serializers.IntegerField(required=False, allow_null=True)
    fulfillment_type = serializers.CharField(required=False)

    selected_partner_id = serializers.IntegerField(
        required=True
    )
    
    @transaction.atomic
    def create(self, validated_data):
        tenant = self.context["tenant"]
        user = self.context["request"].user

        items_data = validated_data["items"]
        booking_id = validated_data["booking_id"]

        address_id = validated_data.get("address_id")
        fulfillment_type = validated_data.get("fulfillment_type", "on_site")

        # 🔥 Ambil address
        address = None
        address_snapshot = None

        if address_id:
            address = get_user_address_by_id(
                tenant=tenant,
                user=user,
                address_id=address_id
            )

            if not address:
                raise serializers.ValidationError("Alamat tidak valid")

            # 🔥 SNAPSHOT
            address_snapshot = {
                "label": address.label,
                "recipient_name": address.recipient_name,
                "phone": address.phone,
                "address_line": address.address_line,
                "city": address.city,
                "region": address.region,
                "postal_code": address.postal_code,
                "country": address.country,
                "latitude": float(address.latitude) if address.latitude else None,
                "longitude": float(address.longitude) if address.longitude else None,
            }

        # 🔥 VALIDATION (penting!)
        if fulfillment_type in ["delivery", "on_site"] and not address:
            raise serializers.ValidationError(
                "Alamat wajib untuk delivery/on_site"
            )
        
        selected_partner_id = validated_data.get("selected_partner_id")

        selected_partner = get_partner_by_id(
            tenant=tenant,
            partner_id=selected_partner_id
        )

        if not selected_partner:
            raise serializers.ValidationError("Partner tidak valid")
        
        transport_distance = Decimal("0")
        transport_fee = Decimal("0")

        partner_lat = getattr(selected_partner, "search_latitude", None)
        partner_lng = getattr(selected_partner, "search_longitude", None)

        customer_lat = None
        customer_lng = None

        if address:
            customer_lat = address.latitude
            customer_lng = address.longitude

        if (
            fulfillment_type == "on_site"
            and partner_lat is not None
            and partner_lng is not None
            and customer_lat is not None
            and customer_lng is not None
        ):
            km = calculate_distance_km(
                float(partner_lat),
                float(partner_lng),
                float(customer_lat),
                float(customer_lng),
            )

            transport_distance = Decimal(str(round(km, 2)))
            transport_fee = calculate_transport_fee(km)

        listings = PartnerListing.objects.filter(
            id__in=[i["id"] for i in items_data],
            tenant=tenant,
            is_active=True,
        )

        listing_map = {l.id: l for l in listings}

        if len(listing_map) != len(items_data):
            raise serializers.ValidationError("Listing tidak valid")

        total = Decimal("0")

        order = Order.objects.create(
            tenant=tenant,
            user=user,
            order_number=str(uuid.uuid4())[:12],
            total_amount=0,
            booking_id=booking_id,
            fulfillment_type=fulfillment_type,
            address=address,
            address_snapshot=address_snapshot,
            selected_partner=selected_partner,
            payment_status=PaymentStatus.UNPAID,  # 🔥 NEW
            status=OrderStatus.PENDING, 
            transport_distance_km=transport_distance,
            transport_fee_amount=transport_fee,
        )

        order_items = []

        for item in items_data:
            listing = listing_map[item["id"]]
            qty = item["qty"]

            price = Decimal(listing.price)
            subtotal = price * qty
            total += subtotal

            order_items.append(
                OrderItem(
                    order=order,
                    listing=listing,
                    quantity=qty,
                    price=price,
                )
            )

        OrderItem.objects.bulk_create(order_items)

        # =========================
        # APPLY FEE ENGINE
        # =========================
        engine = FeeEngine()

        result = engine.calculate(
            FeeInput(
                tenant_id=str(tenant.id),
                amount=total,
                partner_id=selected_partner.id,
            )
        )

        # 🔥 UPDATE TOTAL (customer bayar)
        order.subtotal_amount = total
        order.total_fee_amount = (
            result.total_customer_fee + transport_fee
        )
        order.total_amount = (
            result.final_customer_pay + transport_fee
        )        
        order.save(update_fields=[
            "subtotal_amount",
            "total_fee_amount",
            "total_amount",
        ])

        # =========================
        # SNAPSHOT FEE
        # =========================
        for fee in result.customer_fees + result.partner_fees:
            OrderFee.objects.create(
                order_id=order.id,
                fee_name=fee.name,
                fee_type=fee.fee_type,
                applies_to=fee.applies_to,
                value=fee.value,
                amount=fee.amount,
            )

        return order