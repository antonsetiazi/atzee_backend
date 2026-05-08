# accounting/api/payable_payments/serializers.py

from rest_framework import serializers

from accounting.models import (
    PayablePayment,
    PayableAllocation,
)


class PayableAllocationSerializer(
    serializers.ModelSerializer
):

    invoice_number = serializers.CharField(
        source="invoice.invoice_number",
        read_only=True
    )

    class Meta:
        model = PayableAllocation

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


class PayablePaymentSerializer(
    serializers.ModelSerializer
):

    allocations = PayableAllocationSerializer(
        many=True
    )

    partner_name = serializers.CharField(
        source="partner.name",
        read_only=True
    )

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

            "allocations",
        ]