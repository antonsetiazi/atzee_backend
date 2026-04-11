# marketplace/serializers/order_output_serializer.py

from rest_framework import serializers
from marketplace.models.order import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="listing.product.name")

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "name",
            "quantity",
            "price",
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    address = serializers.JSONField(source="address_snapshot", read_only=True)

    selected_partner = serializers.SerializerMethodField()
    partner = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()

    payment_status = serializers.CharField(read_only=True)
    bookingId = serializers.SerializerMethodField()

    def get_bookingId(self, obj):
        return obj.booking_id
    
    def get_customer(self, obj):
        user = obj.user
        if not user:
            return None

        full_name = getattr(user, "full_name", None)
        username = getattr(user, "username", None)
        phone = getattr(user, "phone", None)

        return {
            "id": user.id,
            "name": full_name or username or "Customer",
            "phone": phone,
        }
    
    def get_selected_partner(self, obj):
        if not obj.selected_partner:
            return None
        
        return {
            "id": obj.selected_partner.id,
            "name": obj.selected_partner.name,
        }

    def get_partner(self, obj):
        if not obj.partner:
            return None
        
        return {
            "id": obj.partner.id,
            "name": obj.partner.name,
            "phone": obj.partner.phone,
        }
    
    class Meta:
        model = Order
        fields = [
            "id",
            "order_number",
            "status",
            "payment_status",
            "total_amount",
            "fulfillment_type",
            "address",
            "customer",
            "selected_partner",
            "partner",
            "created_at",
            "bookingId",
            "items",
        ]