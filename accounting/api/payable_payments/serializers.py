# accounting/api/payable_payments/serializers.py

from rest_framework import serializers

from accounting.models import (
    PayableAllocation,
    PayablePayment,
)


class PayableAllocationReadSerializer(serializers.ModelSerializer):

    invoice_number = serializers.CharField(
        source="invoice.invoice_number",
        read_only=True,
    )

    invoice_date = serializers.DateField(
        source="invoice.invoice_date",
        read_only=True,
    )

    invoice_total = serializers.DecimalField(
        source="invoice.total_amount",
        max_digits=18,
        decimal_places=2,
        read_only=True,
    )

    invoice_status = serializers.CharField(
        source="invoice.status",
        read_only=True,
    )

    class Meta:
        model = PayableAllocation
        fields = [
            "id",
            "invoice",
            "invoice_number",
            "invoice_date",
            "invoice_total",
            "invoice_status",
            "allocated_amount",
        ]


class PayableAllocationWriteSerializer(serializers.Serializer):
    invoice_id = serializers.UUIDField()
    allocated_amount = serializers.DecimalField(
        max_digits=18, decimal_places=2
    )


class PayablePaymentReadSerializer(serializers.ModelSerializer):
    allocations = PayableAllocationReadSerializer(many=True)
    partner_name = serializers.CharField(source="partner.name", read_only=True)

    class Meta:
        model = PayablePayment
        fields = [
            "id",
            "partner",
            "partner_name",
            "payment_number",
            "payment_date",
            "amount",
            "payment_method",
            "reference",
            "notes",
            "status",
            "allocations",
        ]


class PayablePaymentCreateSerializer(serializers.Serializer):
    partner_id = serializers.UUIDField()
    payment_number = serializers.CharField()
    payment_date = serializers.DateField()
    amount = serializers.DecimalField(max_digits=18, decimal_places=2)
    payment_method = serializers.CharField()
    reference = serializers.CharField(required=False, allow_blank=True)
    notes = serializers.CharField(required=False, allow_blank=True)
    allocations = PayableAllocationWriteSerializer(many=True)
