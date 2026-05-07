# accounting/api/receivable_payments/serializers.py

from rest_framework import serializers

from accounting.models import (
    ReceivablePayment,
    ReceivableAllocation,
)


class ReceivableAllocationSerializer(
    serializers.ModelSerializer
):

    invoice_number = serializers.CharField(
        source="invoice.invoice_number",
        read_only=True
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


class ReceivablePaymentSerializer(
    serializers.ModelSerializer
):

    allocations = ReceivableAllocationSerializer(
        many=True
    )

    customer_name = serializers.CharField(
        source="customer.name",
        read_only=True
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