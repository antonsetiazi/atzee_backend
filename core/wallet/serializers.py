# core/wallet/serializers.py

from rest_framework import serializers
from core.wallet.models import Wallet, WalletTransaction


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "user", "balance"]


class WalletTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletTransaction
        fields = [
            "id",
            "wallet",
            "amount",
            "transaction_type",
            "reference",
            "description",
            "created_at",
        ]


class WalletTopUpSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=18, decimal_places=2)
    description = serializers.CharField(required=False, allow_blank=True)