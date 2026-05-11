# accounting/api/fixed_asset_depreciation/serializers.py

from rest_framework import serializers


class FixedAssetDepreciationRunSerializer(serializers.Serializer):

    period_date = serializers.DateField()
