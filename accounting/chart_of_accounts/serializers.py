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
            "is_postable",
        ]


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = [
            "id",
            "code",
            "name",
            "account_type",
            "parent",
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

    def create(self, validated_data):
        request = self.context["request"]

        return services.create_account(
            tenant=request.tenant,
            created_by=request.user,
            **validated_data
        )
