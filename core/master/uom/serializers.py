# core/master/uom/serializers.py

from rest_framework import serializers
from core.master.uom.models import UOM, UOMCategory


class UOMCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UOMCategory
        fields = [
            "id",
            "code",
            "name",
        ]


class UOMListSerializer(serializers.ModelSerializer):
    category = UOMCategorySerializer()

    class Meta:
        model = UOM
        fields = [
            "id",
            "code",
            "name",
            "symbol",
            "precision",
            "is_base",
            "category",
        ]


class UOMDetailSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(
        source="category.id",
        allow_null=True,
    )

    class Meta:
        model = UOM
        fields = [
            "id",
            "code",
            "name",
            "symbol",
            "precision",
            "is_base",
            "category_id",
            "created_at",
            "updated_at",
        ]


class UOMCreateSerializer(serializers.Serializer):
    category_id = serializers.IntegerField()
    code = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=100)
    symbol = serializers.CharField(required=False, allow_blank=True)
    precision = serializers.IntegerField(required=False)
    is_base = serializers.BooleanField(required=False)


class UOMUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    symbol = serializers.CharField(required=False, allow_blank=True)
    precision = serializers.IntegerField(required=False)
    is_base = serializers.BooleanField(required=False)
    is_active = serializers.BooleanField(required=False)
