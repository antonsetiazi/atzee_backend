# accounting/api/fixed_assets/serializers.py

from rest_framework import serializers

from accounting.models import (
    FixedAsset,
)


class FixedAssetReadSerializer(serializers.ModelSerializer):
    category_id = serializers.UUIDField(
        source="category.id",
        read_only=True,
    )

    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    class Meta:
        model = FixedAsset

        fields = [
            "id",
            "asset_number",
            "name",
            "description",
            "category_id",
            "category",
            "category_name",
            "serial_number",
            "location",
            "purchase_date",
            "capitalization_date",
            "purchase_cost",
            "salvage_value",
            "depreciation_method",
            "useful_life_months",
            "depreciation_start_date",
            "last_depreciation_date",
            "accumulated_depreciation",
            "book_value",
            "status",
        ]


class FixedAssetCreateSerializer(serializers.Serializer):
    asset_number = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField(required=False, allow_blank=True)
    category_id = serializers.UUIDField()
    serial_number = serializers.CharField(required=False, allow_blank=True)
    location = serializers.CharField(required=False, allow_blank=True)
    purchase_date = serializers.DateField()
    capitalization_date = serializers.DateField()
    purchase_cost = serializers.DecimalField(max_digits=18, decimal_places=2)
    depreciation_start_date = serializers.DateField()
    salvage_value = serializers.DecimalField(
        max_digits=18, decimal_places=2, required=False
    )
