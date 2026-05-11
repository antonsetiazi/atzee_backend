# accounting/api/asset_disposals/serializers.py

from rest_framework import serializers

from accounting.models import (
    AssetDisposal,
)


class AssetDisposalReadSerializer(serializers.ModelSerializer):

    asset_number = serializers.CharField(
        source="asset.asset_number",
        read_only=True,
    )

    asset_name = serializers.CharField(
        source="asset.name",
        read_only=True,
    )

    class Meta:
        model = AssetDisposal

        fields = [
            "id",
            "asset",
            "asset_number",
            "asset_name",
            "disposal_date",
            "disposal_value",
            "gain_loss_amount",
            "notes",
            "status",
        ]


class AssetDisposalCreateSerializer(serializers.Serializer):

    asset_id = serializers.UUIDField()

    disposal_date = serializers.DateField()

    disposal_value = serializers.DecimalField(
        max_digits=18,
        decimal_places=2,
    )

    notes = serializers.CharField(
        required=False,
        allow_blank=True,
    )
