from rest_framework import serializers

from accounting.chart_of_accounts.models import ChartOfAccount
from accounting.chart_of_accounts import services


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = [
            "id",
            "code",
            "name",
            "account_type",
            "is_active",
            "is_postable",
        ]


class AccountDetailSerializer(serializers.ModelSerializer):
    parent_id = serializers.IntegerField(
        source="parent.id",
        allow_null=True,
        required=False,
    )

    class Meta:
        model = ChartOfAccount
        fields = [
            "id",
            "code",
            "name",
            "account_type",
            "parent_id",
            "is_active",
            "is_postable",
            "is_system",
            "created_at",
            "updated_at",
        ]


class AccountCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=255)
    account_type = serializers.CharField()
    parent_id = serializers.IntegerField(required=False)
    is_postable = serializers.BooleanField(default=True)
    is_active = serializers.BooleanField(default=True)


class AccountUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=255)
    account_type = serializers.CharField()
    parent_id = serializers.IntegerField(required=False)
    is_postable = serializers.BooleanField(default=True)
    is_active = serializers.BooleanField(default=True)

