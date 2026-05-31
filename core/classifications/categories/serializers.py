# core/classifications/categories/serializers.py

from rest_framework import serializers

from core.classifications.categories.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "code",
            "name",
            "scope",
            "parent",
            "icon_url",
            "color",
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    parent_id = serializers.IntegerField(
        source="parent.id",
        allow_null=True,
    )

    class Meta:
        model = Category
        fields = [
            "id",
            "code",
            "name",
            "scope",
            "parent_id",
            "icon_url",
            "color",
            "created_at",
            "updated_at",
        ]


class CategoryCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)
    scope = serializers.CharField(max_length=50)
    icon_url = serializers.URLField(required=False, allow_blank=True)
    color = serializers.CharField(required=False, allow_blank=True)
    parent_id = serializers.IntegerField(required=False, allow_null=True)


class CategoryUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    scope = serializers.CharField(required=False)
    icon_url = serializers.URLField(required=False, allow_blank=True)
    color = serializers.CharField(required=False, allow_blank=True)
    parent_id = serializers.IntegerField(required=False, allow_null=True)
    is_active = serializers.BooleanField(required=False)
