# business/transactions/serializers.py

from rest_framework import serializers
from decimal import Decimal

from business.transactions.models.transaction import Transaction
from business.transactions.models.transaction_item import TransactionItem
from business.transactions.models.enums import (
    TransactionType,
    TransactionSubType,
    TransactionStatus,
)
from business.transactions import services


class TransactionItemSerializer(serializers.ModelSerializer):
    transaction_id = serializers.IntegerField(source="transaction.id")
    product_id = serializers.IntegerField(source="product.id")
    product_name = serializers.CharField(source="product.name")

    class Meta:
        model = TransactionItem
        fields = [
            "id",
            "transaction_id",
            "product_id",
            "product_name",
            "quantity",
            "unit_price",
            "total_price",
            "notes",
        ]


class TransactionDetailSerializer(serializers.ModelSerializer):
    items = TransactionItemSerializer(many=True)

    customer_id = serializers.IntegerField(
        source="customer.id",
        allow_null=True
    )
    partner_id = serializers.IntegerField(
        source="partner.id",
        allow_null=True
    )

    class Meta:
        model = Transaction
        fields = [
            "id",
            "reference",
            "transaction_type",
            "subtype",
            "status",
            "transaction_date",
            "customer_id",
            "partner_id",
            "notes",
            "items",
            "created_at",
            "updated_at",
        ]


class TransactionListSerializer(serializers.ModelSerializer):
    total_items = serializers.IntegerField(
        source="items.count",
        read_only=True
    )

    class Meta:
        model = Transaction
        fields = [
            "id",
            "reference",
            "transaction_type",
            "subtype",
            "status",
            "transaction_date",
            "total_items",
        ]


class TransactionCreateSerializer(serializers.Serializer):
    reference = serializers.CharField(
        max_length=100, 
        required=False, 
        allow_null=True,
        allow_blank=True,
    )
    transaction_date = serializers.DateField()
    customer_id = serializers.IntegerField(required=False)
    partner_id = serializers.IntegerField(required=False)
    notes = serializers.CharField(required=False, allow_blank=True)


class TransactionUpdateSerializer(serializers.Serializer):
    transaction_date = serializers.DateField()
    notes = serializers.CharField(required=False, allow_blank=True)


class TransactionItemAddSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.DecimalField(max_digits=14, decimal_places=4)
    unit_price = serializers.DecimalField(max_digits=14, decimal_places=2)
    notes = serializers.CharField(required=False, allow_blank=True)


class TransactionItemUpdateSerializer(serializers.Serializer):
    quantity = serializers.DecimalField(max_digits=14, decimal_places=4, required=False)
    unit_price = serializers.DecimalField(max_digits=14, decimal_places=2, required=False)
    notes = serializers.CharField(required=False, allow_blank=True)


class TransactionConfirmSerializer(serializers.Serializer):
    def save(self, **kwargs):
        request = self.context["request"]
        transaction = self.context["transaction"]

        return services.confirm_transaction(
            tenant=request.tenant,
            transaction_id=transaction.id,
            confirmed_by=request.user,
        )


class TransactionCancelSerializer(serializers.Serializer):
    reason = serializers.CharField(required=False, allow_blank=True)

    def save(self, **kwargs):
        request = self.context["request"]
        transaction = self.context["transaction"]

        return services.cancel_transaction(
            tenant=request.tenant,
            transaction_id=transaction.id,
            cancelled_by=request.user,
            reason=self.validated_data.get("reason"),
        )
