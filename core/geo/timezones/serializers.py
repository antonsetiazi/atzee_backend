# core/geo/timezones/serializers.py

from rest_framework import serializers
from core.geo.timezones.models import Timezone


class TimezoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ["id", "name", "utc_offset"]


class TimezoneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = "__all__"


class TimezoneCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    utc_offset = serializers.CharField(max_length=10)


class TimezoneUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    utc_offset = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
