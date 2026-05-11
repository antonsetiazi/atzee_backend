# accounting/api/asset_categories/serializers.py

from rest_framework import serializers

from accounting.models import AssetCategory


class AssetCategoryReadSerializer(serializers.ModelSerializer):
    asset_account_id = serializers.UUIDField(
        source="asset_account.id", read_only=True
    )
    asset_account_name = serializers.CharField(
        source="asset_account.name",
        read_only=True,
    )

    accumulated_depreciation_account_id = serializers.UUIDField(
        source="accumulated_depreciation_account.id",
        read_only=True,
    )
    accumulated_depreciation_account_name = serializers.CharField(
        source="accumulated_depreciation_account.name",
        read_only=True,
    )

    depreciation_expense_account_id = serializers.UUIDField(
        source="depreciation_expense_account.id",
        read_only=True,
    )
    depreciation_expense_account_name = serializers.CharField(
        source="depreciation_expense_account.name",
        read_only=True,
    )

    class Meta:
        model = AssetCategory

        fields = [
            "id",
            "code",
            "name",
            "description",
            "asset_account_id",
            "asset_account_name",
            "accumulated_depreciation_account_id",
            "accumulated_depreciation_account_name",
            "depreciation_expense_account_id",
            "depreciation_expense_account_name",
            "depreciation_method",
            "useful_life_months",
            "salvage_value_percent",
            "is_active",
        ]


class AssetCategoryCreateSerializer(serializers.ModelSerializer):
    asset_account_id = serializers.UUIDField(write_only=True)
    accumulated_depreciation_account_id = serializers.UUIDField(
        write_only=True
    )
    depreciation_expense_account_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = AssetCategory
        fields = [
            "code",
            "name",
            "description",
            "asset_account_id",
            "accumulated_depreciation_account_id",
            "depreciation_expense_account_id",
            "depreciation_method",
            "useful_life_months",
            "salvage_value_percent",
        ]


# class AssetCategoryCreateSerializer(serializers.Serializer):
#     code = serializers.CharField(max_length=50)
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField(
#         required=False,
#         allow_blank=True,
#     )
#     asset_account_id = serializers.UUIDField()
#     accumulated_depreciation_account_id = serializers.UUIDField()
#     depreciation_expense_account_id = serializers.UUIDField()
#     depreciation_method = serializers.CharField()
#     useful_life_months = serializers.IntegerField()
#     salvage_value_percent = serializers.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#         required=False,
#         default=0,
#     )
