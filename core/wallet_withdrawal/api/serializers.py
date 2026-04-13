# core/wallet_withdrawal/api/serializers.py

from rest_framework import serializers
from core.wallet_withdrawal.models.withdrawal import Withdrawal


class WithdrawalRequestSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=18, decimal_places=2)
    destination = serializers.JSONField()


class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdrawal
        fields = [
            "id",
            "amount",
            "fee",
            "status",
            "destination",
            "created_at",
            "processed_at",
        ]