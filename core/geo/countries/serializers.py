# core/geo/countries/serializers.py

from rest_framework import serializers
from core.geo.countries.models import Country


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "code", "name"]


class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CountryCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=5)
    name = serializers.CharField(max_length=100)
    phone_code = serializers.CharField(required=False, allow_blank=True)
    currency_code = serializers.CharField(required=False, allow_blank=True)


class CountryUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    phone_code = serializers.CharField(required=False, allow_blank=True)
    currency_code = serializers.CharField(required=False, allow_blank=True)
    is_active = serializers.BooleanField(required=False)
