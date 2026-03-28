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

    class Meta:
        model = Order
        fields = [
            "id",
            "order_number",
            "status",
            "total_amount",
            "created_at",
            "items",
        ]