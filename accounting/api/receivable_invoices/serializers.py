# accounting/api/receivable_invoices/serializers.py

from rest_framework import serializers

from accounting.models import (
    ReceivableInvoice,
    ReceivableInvoiceItem,
)


class ReceivableInvoiceItemSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = ReceivableInvoiceItem

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


class ReceivableInvoiceSerializer(
    serializers.ModelSerializer
):

    items = ReceivableInvoiceItemSerializer(
        many=True
    )

    customer_name = serializers.CharField(
        source="customer.name",
        read_only=True
    )

    class Meta:
        model = ReceivableInvoice

        fields = [
            "id",

            "customer",
            "customer_name",

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
            "subtotal",
            "tax_amount",
            "total_amount",

            "paid_amount",
            "balance_due",

            "status",
        ]