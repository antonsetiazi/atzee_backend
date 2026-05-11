# accounting/api/payable_invoices/serializers.py

from rest_framework import serializers

from accounting.models import (
    PayableInvoice,
    PayableInvoiceItem,
)


class PayableInvoiceItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PayableInvoiceItem

        fields = [
            "id",
            "description",
            "qty",
            "unit_price",
            "total",
        ]

        read_only_fields = [
            "id",
            "total",
        ]


class PayableInvoiceSerializer(serializers.ModelSerializer):
    items = PayableInvoiceItemSerializer(many=True)
    partner_name = serializers.CharField(source="partner.name", read_only=True)

    class Meta:
        model = PayableInvoice

        fields = [
            "id",
            "partner",
            "partner_name",
            "invoice_number",
            "invoice_date",
            "due_date",
            "notes",
            "subtotal",
            "tax_amount",
            "total_amount",
            "paid_amount",
            "balance_due",
            "status",
            "items",
        ]

        read_only_fields = [
            "id",
            "subtotal",
            "tax_amount",
            "total_amount",
            "paid_amount",
            "balance_due",
            "status",
        ]


class PayableInvoiceCreateSerializer(serializers.Serializer):
    partner_id = serializers.IntegerField()
    invoice_number = serializers.CharField()
    invoice_date = serializers.DateField()
    due_date = serializers.DateField()
    tax_id = serializers.UUIDField(
        required=False,
        allow_null=True,
    )
    notes = serializers.CharField(required=False, allow_blank=True)
    items = PayableInvoiceItemSerializer(many=True)
