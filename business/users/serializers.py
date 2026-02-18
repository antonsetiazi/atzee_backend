# business/users/serializers.py

from rest_framework import serializers
from business.users.models import BusinessUser


class BusinessUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUser
        fields = [
            "id",
            "name",
            "phone",
            "organization_name",
        ]


class BusinessUserDetailSerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(
        max_digits=9,
        decimal_places=6,
        required=False,
        allow_null=True
    )

    longitude = serializers.DecimalField(
        max_digits=9,
        decimal_places=6,
        required=False,
        allow_null=True
    )

    class Meta:
        model = BusinessUser
        fields = "__all__"


class BusinessUserCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_null=True)
    organization_name = serializers.CharField(required=False, allow_blank=True)
    organization_type = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    notes = serializers.CharField(required=False, allow_blank=True)
    extensions = serializers.JSONField(required=False)


class BusinessUserUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_null=True)
    organization_name = serializers.CharField(required=False, allow_blank=True)
    organization_type = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    latitude = serializers.FloatField(
        required=False,
        allow_null=True
    )

    longitude = serializers.FloatField(
        required=False,
        allow_null=True
    )
    notes = serializers.CharField(required=False, allow_blank=True)
    extensions = serializers.JSONField(required=False)