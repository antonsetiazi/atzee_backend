# core/master/locations/serializers.py

from rest_framework import serializers
from core.master.locations.models import Location


class LocationListSerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(
        source="parent.name",
        read_only=True
    )

    class Meta:
        model = Location
        fields = [
            "id",
            "code",
            "name",
            "parent_name",
            "is_active",
        ]


class LocationDetailSerializer(serializers.ModelSerializer):
    parent_id = serializers.IntegerField(
        source="parent.id",
        allow_null=True,
        required=False
    )

    class Meta:
        model = Location
        fields = [
            "id",
            "code",
            "name",
            "description",
            "parent_id",
            "is_active",
            "created_at",
            "updated_at",
        ]


class LocationCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(
        required=False,
        allow_blank=True
    )
    parent_id = serializers.IntegerField(
        required=False,
        allow_null=True
    )
    is_active = serializers.BooleanField(required=False)


class LocationUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(
        required=False,
        allow_blank=True
    )
    parent_id = serializers.IntegerField(
        required=False,
        allow_null=True
    )
    is_active = serializers.BooleanField(required=False)
