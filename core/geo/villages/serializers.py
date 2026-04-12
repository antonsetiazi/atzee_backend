# core/geo/villages/serializers.py

from rest_framework import serializers
from core.geo.villages.models import Village


class VillageListSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source="country.name")
    region_name = serializers.CharField(source="region.name")
    city_name = serializers.CharField(source="city.name")
    district_name = serializers.CharField(source="district.name")

    class Meta:
        model = Village
        fields = [
            "id",
            "code",
            "name",
            "country",
            "country_name",
            "region",
            "region_name",
            "city",
            "city_name",
            "district",
            "district_name",
        ]


class VillageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = "__all__"


class VillageCreateSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()
    region_id = serializers.IntegerField()
    city_id = serializers.IntegerField()
    district_id = serializers.IntegerField()
    code = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=100)
    center_latitude = serializers.FloatField(required=False)
    center_longitude = serializers.FloatField(required=False)


class VillageUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    center_latitude = serializers.FloatField(required=False)
    center_longitude = serializers.FloatField(required=False)
    is_active = serializers.BooleanField(required=False)