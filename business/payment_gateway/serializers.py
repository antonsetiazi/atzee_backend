# business/payment_gateway/serializers.py

from rest_framework import serializers
from business.payment_gateway.models import (
    PaymentMethod,
    PaymentGatewayConfig
)


# ------------------------------
# PAYMENT METHOD
# ------------------------------

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = [
            "id",
            "name",
            "code",
            "provider",
            "is_active",
            "order",
            "config",
        ]
        read_only_fields = ["id"]


# ------------------------------
# GATEWAY CONFIG
# ------------------------------

class PaymentGatewayConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentGatewayConfig
        fields = [
            "id",
            "provider",
            "environment",
            "is_active",
            "api_key",
            "secret_key",
            "merchant_id",
            "extra_config",
        ]
        read_only_fields = ["id"]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # 🔐 hide secret
        if data.get("api_key"):
            data["api_key"] = "****"
        if data.get("secret_key"):
            data["secret_key"] = "****"

        return data


class PaymentMethodPublicSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="code")
    label = serializers.CharField(source="name")

    class Meta:
        model = PaymentMethod
        fields = ["id", "label"]        