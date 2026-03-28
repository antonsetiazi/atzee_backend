# marketplace/serializers/order_serializer.py

from rest_framework import serializers
from marketplace.models.order import Order, OrderItem
from marketplace.models.listing import PartnerListing
import uuid


class OrderItemInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    qty = serializers.IntegerField(min_value=1)


class CreateOrderSerializer(serializers.Serializer):
    items = OrderItemInputSerializer(many=True)
    payment_method = serializers.CharField()

    def create(self, validated_data):
        tenant = self.context["tenant"]
        user = self.context["request"].user

        items_data = validated_data["items"]

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
        order.save()

        return order