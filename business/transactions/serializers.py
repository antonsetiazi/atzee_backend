from rest_framework import serializers
from decimal import Decimal

from business.transactions.models.transaction import Transaction
from business.transactions.models.transaction_item import TransactionItem
from business.transactions.models.enums import (
    TransactionType,
    TransactionStatus,
)
from business.transactions import services


class TransactionItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="product.id")
    product_name = serializers.CharField(source="product.name")

    class Meta:
        model = TransactionItem
        fields = [
            "id",
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
            "status",
            "transaction_date",
            "total_items",
        ]


class TransactionCreateSerializer(serializers.Serializer):
    reference = serializers.CharField(max_length=100)
    transaction_type = serializers.ChoiceField(
        choices=TransactionType.choices
    )
    transaction_date = serializers.DateField()
    customer_id = serializers.IntegerField(required=False)
    partner_id = serializers.IntegerField(required=False)
    notes = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        request = self.context["request"]

        customer = None
        partner = None

        if "customer_id" in validated_data:
            from business.customers.selectors import get_customer_by_id
            customer = get_customer_by_id(
                tenant=request.tenant,
                customer_id=validated_data.pop("customer_id"),
            )

        if "partner_id" in validated_data:
            from business.partners.selectors import get_partner_by_id
            partner = get_partner_by_id(
                tenant=request.tenant,
                partner_id=validated_data.pop("partner_id"),
            )

        return services.create_transaction(
            tenant=request.tenant,
            created_by=request.user,
            customer=customer,
            partner=partner,
            **validated_data
        )


class TransactionItemAddSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.DecimalField(max_digits=14, decimal_places=4)
    unit_price = serializers.DecimalField(max_digits=14, decimal_places=2)
    notes = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        request = self.context["request"]
        transaction = self.context["transaction"]

        from business.products.selectors import get_product_by_id

        product = get_product_by_id(
            tenant=request.tenant,
            product_id=validated_data.pop("product_id"),
        )

        if not product:
            raise serializers.ValidationError("Product not found.")

        return services.add_transaction_item(
            tenant=request.tenant,
            transaction_id=transaction.id,
            product=product,
            created_by=request.user,
            **validated_data
        )


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
