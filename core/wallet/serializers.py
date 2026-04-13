# core/wallet/serializers.py

from rest_framework import serializers
from core.wallet.models import Wallet, WalletTransaction


# ==============================
# WALLET
# ==============================

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = [
            "available_balance",
            "held_balance",
        ]
        read_only_fields = fields


# ==============================
# TRANSACTIONS
# ==============================

class WalletTransactionSerializer(serializers.ModelSerializer):
    direction = serializers.SerializerMethodField()

    def get_direction(self, obj):
        return "in" if obj.amount > 0 else "out"
    class Meta:
        model = WalletTransaction
        fields = [
            "id",
            "amount",
            "direction",
            "transaction_type",
            "reference_type",
            "reference_id",
            "description",
            "created_at",
        ]


# ==============================
# INPUT
# ==============================

class WalletTopUpSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=18, decimal_places=2)
    description = serializers.CharField(required=False, allow_blank=True)