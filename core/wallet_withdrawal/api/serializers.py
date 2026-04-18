# core/wallet_withdrawal/api/serializers.py

from rest_framework import serializers
from core.wallet_withdrawal.models.withdrawal import Withdrawal


class WithdrawalRequestSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=18, decimal_places=2)
    destination_bank_id = serializers.UUIDField()


class WithdrawalSerializer(serializers.ModelSerializer):
    user_bank_id = serializers.SerializerMethodField()

    def get_user_bank_id(self, obj):
        return obj.destination.get("user_bank_id")
    
    class Meta:
        model = Withdrawal
        fields = [
            "id",
            "amount",
            "fee",
            "status",
            "destination",
            "user_bank_id",
            "created_at",
            "processed_at",
        ]