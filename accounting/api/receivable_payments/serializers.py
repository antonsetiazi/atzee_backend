# accounting/api/receivable_payments/serializers.py

from rest_framework import serializers

from accounting.models import (
    ReceivableAllocation,
    ReceivablePayment,
)


class ReceivableAllocationSerializer(serializers.ModelSerializer):
    invoice_number = serializers.CharField(
        source="invoice.invoice_number", read_only=True
    )

    class Meta:
        model = ReceivableAllocation

        fields = [
            "id",
            "invoice",
            "invoice_number",
            "allocated_amount",
        ]

        read_only_fields = [
            "id",
            "invoice_number",
        ]


class ReceivableAllocationCreateSerializer(serializers.Serializer):
    invoice_id = serializers.UUIDField()
    allocated_amount = serializers.DecimalField(
        max_digits=18, decimal_places=2
    )


class ReceivablePaymentSerializer(serializers.ModelSerializer):
    allocations = ReceivableAllocationSerializer(many=True)
    customer_name = serializers.CharField(
        source="customer.name", read_only=True
    )

    class Meta:
        model = ReceivablePayment

        fields = [
            "id",
            "customer",
            "customer_name",
            "payment_number",
            "payment_date",
            "amount",
            "payment_method",
            "reference",
            "notes",
            "allocations",
        ]


class ReceivablePaymentCreateSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    payment_number = serializers.CharField()
    payment_date = serializers.DateField()
    payment_method = serializers.CharField()
    amount = serializers.DecimalField(max_digits=18, decimal_places=2)
    allocations = ReceivableAllocationCreateSerializer(many=True)
    notes = serializers.CharField(required=False, allow_blank=True)
