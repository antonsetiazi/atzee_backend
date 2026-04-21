# business/partners/serializers.py

from rest_framework import serializers
from business.partners.models import Partner
from business.partners import services


class PartnerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            "id",
            "code",
            "name",
            "phone",
            "email",
            "base_price",
            "rating_avg",
            "rating_count",
        ]


class PartnerDetailSerializer(serializers.ModelSerializer):
    location_label = serializers.ReadOnlyField()
    city_name = serializers.ReadOnlyField()

    core_user_id = serializers.IntegerField(
        source="core_user.id",
        read_only=True
    )

    class Meta:
        model = Partner
        fields = [
            "id",
            "core_user_id",
            "code",
            "name",
            "phone",
            "email",
            "address",
            "notes",
            "extensions",
            "search_latitude",
            "search_longitude",
            "location_label",
            "city_name",
            "base_price",
            "rating_avg",
            "rating_count",
            "created_at",
            "updated_at",
        ]


class PartnerCreateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    notes = serializers.CharField(required=False, allow_blank=True)
    extensions = serializers.JSONField(required=False) 
    

class PartnerUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    notes = serializers.CharField(required=False, allow_blank=True)
    extensions = serializers.JSONField(required=False) 
