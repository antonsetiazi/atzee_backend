# core/account/serializers.py

from rest_framework import serializers
from core.account.models import UserSettings, UserAddress


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = [
            "theme",
            "language",
            "timezone",
            "email_notifications",
        ]


class UserAddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"


class UserAddressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"


class UserAddressCreateSerializer(serializers.ModelSerializer):
    is_default = serializers.BooleanField(
        required=False,
        default=False,
        allow_null=False
    )

    class Meta:
        model = UserAddress
        exclude = ["user", "tenant"]


class UserAddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        exclude = ["user", "tenant"]