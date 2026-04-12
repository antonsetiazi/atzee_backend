# core/geo/cities/serializers.py

from rest_framework import serializers
from core.geo.cities.models import City


class CityListSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(
        source="country.name",
        read_only=True
    )
    region_name = serializers.CharField(
        source="region.name",
        read_only=True
    )

    class Meta:
        model = City
        fields = [
            "id",
            "code",
            "name",
            "country",
            "country_name",
            "region",
            "region_name",
        ]


class CityDetailSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(
        source="country.name",
        read_only=True
    )
    region_name = serializers.CharField(
        source="region.name",
        read_only=True
    )

    class Meta:
        model = City
        fields = "__all__"


class CityCreateSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()
    region_id = serializers.IntegerField()
    code = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=100)
    center_latitude = serializers.FloatField(required=False)
    center_longitude = serializers.FloatField(required=False)


class CityUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    center_latitude = serializers.FloatField(required=False)
    center_longitude = serializers.FloatField(required=False)
    is_active = serializers.BooleanField(required=False)