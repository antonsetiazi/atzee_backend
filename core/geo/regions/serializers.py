# core/geo/regions/serializers.py

from rest_framework import serializers
from core.geo.regions.models import Region


class RegionListSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(
        source="country.name",
        read_only=True
    )

    class Meta:
        model = Region
        fields = [
            "id",
            "code",
            "name",
            "country",
            "country_name",
        ]


class RegionDetailSerializer(serializers.ModelSerializer):
    country_id = serializers.IntegerField(
        source="country.id",
        allow_null=True,
    )

    class Meta:
        model = Region
        fields = [
            "id",
            "code",
            "name",
            "country_id",
            "created_at",
            "updated_at",
        ]


class RegionCreateSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()
    code = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=100)


class RegionUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
