# core/master/currencies/serializers.py

from rest_framework import serializers
from core.master.currencies.models import Currency


class CurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            "id",
            "code",
            "name",
            "symbol",
        ]


class CurrencyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            "id",
            "code",
            "name",
            "symbol",
            "decimal_places",
            "is_active",
            "created_at",
            "updated_at",
        ]


class CurrencyCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=50)
    symbol = serializers.CharField(
        max_length=10,
        required=False,
        allow_blank=True
    )
    decimal_places = serializers.IntegerField(required=False)


class CurrencyUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    symbol = serializers.CharField(
        required=False,
        allow_blank=True
    )
    decimal_places = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(required=False)
