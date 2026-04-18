# core/master/banks/serializers.py

from rest_framework import serializers
from core.master.banks.models import Bank


class BankListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            "id",
            "code",
            "name",
            "short_name",
        ]


class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            "id",
            "code",
            "name",
            "short_name",
            "sort_order",
            "is_active",
            "created_at",
            "updated_at",
        ]


class BankCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=100)
    short_name = serializers.CharField(
        max_length=50,
        required=False,
        allow_blank=True,
    )


class BankUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    short_name = serializers.CharField(required=False)
    sort_order = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(required=False)