# accounting/fiscal_period/serializers.py

from rest_framework import serializers
from accounting.fiscal_period.models import FiscalPeriod


class FiscalPeriodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalPeriod
        fields = [
            "id",
            "name",
            "start_date",
            "end_date",
            "is_closed",
            "closed_at",
            "closed_by",
        ]


class FiscalPeriodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalPeriod
        fields = [
            "id",
            "name",
            "start_date",
            "end_date",
            "is_closed",
            "closed_at",
            "closed_by",
            "created_at",
            "updated_at",
        ]


class FiscalPeriodCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    start_date = serializers.DateField()
    end_date = serializers.DateField()


class FiscalPeriodUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
