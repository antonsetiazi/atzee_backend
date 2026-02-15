# core/geo/spatial/serializers.py

from rest_framework import serializers
from core.geo.spatial.models import GeoLocation


class GeoLocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocation
        fields = [
            "id",
            "latitude",
            "longitude",
            "label",
        ]


class GeoLocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocation
        fields = "__all__"


class GeoLocationCreateSerializer(serializers.Serializer):
    related_entity = serializers.CharField(max_length=100)
    related_id = serializers.CharField()
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    label = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.JSONField(required=False)


class GeoLocationUpdateSerializer(serializers.Serializer):
    latitude = serializers.DecimalField(
        max_digits=9,
        decimal_places=6,
        required=False
    )
    longitude = serializers.DecimalField(
        max_digits=9,
        decimal_places=6,
        required=False
    )
    label = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.JSONField(required=False)
