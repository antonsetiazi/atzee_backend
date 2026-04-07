# marketplace/serializers/order_serializer.py

from rest_framework import serializers
import uuid

from core.account.selectors import get_user_address_by_id
from business.partners.selectors import get_partner_by_id

from marketplace.models.order import Order, OrderItem
from marketplace.models.order import PaymentStatus, OrderStatus
from marketplace.models.listing import PartnerListing


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

        listings = PartnerListing.objects.filter(
            id__in=[i["id"] for i in items_data],
            tenant=tenant,
            is_active=True,
        )

        listing_map = {l.id: l for l in listings}

        if len(listing_map) != len(items_data):
            raise serializers.ValidationError("Listing tidak valid")

        total = 0

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
        )

        order_items = []

        for item in items_data:
            listing = listing_map[item["id"]]
            qty = item["qty"]

            price = listing.price
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

        order.total_amount = total
        order.save(update_fields=["total_amount"])

        return order