# marketplace/serializers/order_output_serializer.py

from rest_framework import serializers
from marketplace.models.order import Order, OrderItem
from core.fees.models import OrderFee
from business.booking.models import Booking
from business.payment_gateway.models import PaymentGateway

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
    transport_fee = serializers.SerializerMethodField()
    distance_km = serializers.SerializerMethodField()
    platform_fee = serializers.SerializerMethodField()

    items = OrderItemSerializer(many=True, read_only=True)

    address = serializers.JSONField(source="address_snapshot", read_only=True)

    selected_partner = serializers.SerializerMethodField()
    partner = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()

    payment_status = serializers.CharField(read_only=True)
    payment_method = serializers.SerializerMethodField()
    bookingId = serializers.SerializerMethodField()
    fees = serializers.SerializerMethodField()

    booking = serializers.SerializerMethodField()
    partner_earning = serializers.SerializerMethodField()

    def get_transport_fee(self, obj):
        return int(obj.transport_fee_amount or 0)

    def get_distance_km(self, obj):
        if not obj.transport_distance_km:
            return 0
        return float(obj.transport_distance_km)

    def get_platform_fee(self, obj):
        """
        total_fee_amount = platform fee + transport fee
        Maka platform fee = total_fee - transport
        """
        total_fee = obj.total_fee_amount or 0
        transport = obj.transport_fee_amount or 0
        result = total_fee - transport

        if result < 0:
            result = 0

        return int(result)

    def get_bookingId(self, obj):
        return obj.booking_id
    
    def get_booking(self, obj):
        if not obj.booking_id:
            return None

        booking = Booking.objects.filter(id=obj.booking_id).first()

        if not booking:
            return None

        return {
            "id": booking.id,
            "start_time": booking.start_time,
            "end_time": booking.end_time,
            "duration": booking.total_duration,
            "status": booking.status,
        }
    
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
            "owner_user_id": (
                obj.selected_partner.core_user.id
                if obj.selected_partner.core_user
                else None
            ),
        }

    def get_partner(self, obj):
        if not obj.partner:
            return None
        
        return {
            "id": obj.partner.id,
            "name": obj.partner.name,
            "phone": obj.partner.phone,
            "owner_user_id": (
                obj.partner.core_user.id
                if obj.partner.core_user
                else None
            ),
        }
    
    def get_fees(self, obj):
        fees = OrderFee.objects.filter(order_id=obj.id)

        return [
            {
                "name": f.fee_name,
                "amount": f.amount,
                "type": f.fee_type,
                "applies_to": f.applies_to,
            }
            for f in fees
        ]
    
    def get_partner_earning(self, obj):
        fees = OrderFee.objects.filter(order_id=obj.id)

        subtotal = obj.subtotal_amount or 0
        transport = obj.transport_fee_amount or 0

        partner_fee = 0

        for f in fees:
            if f.applies_to == "partner":
                partner_fee += f.amount

        total = subtotal + transport - partner_fee

        if total < 0:
            total = 0

        return int(total)
    
    def get_payment_method(self, obj):
        # 🔹 1. cek gateway dulu
        payment = (
            PaymentGateway.objects
            .filter(
                tenant=obj.tenant,
                reference_type="order",
                reference_id=str(obj.id),
                status=PaymentGateway.STATUS_SUCCESS,
            )
            .order_by("-created_at")
            .first()
        )

        if payment:
            return payment.channel or payment.provider

        # 🔹 2. fallback → WALLET
        if obj.payment_status == "paid":
            return "wallet"

        return None
    
    class Meta:
        model = Order
        fields = [
            "id",
            "order_number",
            "status",
            "payment_status",
            "payment_method",
            "subtotal_amount",
            "total_fee_amount",
            "platform_fee",
            "transport_fee",
            "distance_km",
            "total_amount",
            "partner_earning",
            "fulfillment_type",
            "address",
            "customer",
            "selected_partner",
            "partner",
            "created_at",
            "bookingId",
            "booking",
            "items",
            "fees",
        ]