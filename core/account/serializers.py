# core/account/serializers.py

from rest_framework import serializers
from core.account.models import UserSettings, UserAddress
from core.account.models import UserBankAccount


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


class UserBankSerializer(serializers.ModelSerializer):
    bank_id = serializers.IntegerField(source="bank.id")
    bank_name = serializers.CharField(source="bank.name")

    class Meta:
        model = UserBankAccount
        fields = [
            "id",
            "bank_id",
            "bank_name",
            "account_number",
            "account_name",
            "is_default",
            "is_verified",
            "created_at",
        ]


class UserBankCreateSerializer(serializers.ModelSerializer):
    bank_id = serializers.IntegerField()
    class Meta:
        model = UserBankAccount
        fields = [
            "bank_id",
            "account_number",
            "account_name",
            "is_default",
        ]


class UserBankUpdateSerializer(serializers.ModelSerializer):
    bank_id = serializers.IntegerField()
    class Meta:
        model = UserBankAccount
        fields = [
            "bank_id",
            "account_number",
            "account_name",
            "is_default",
        ]   