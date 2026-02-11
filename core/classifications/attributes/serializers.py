# core/classifications/attributes/serializers.py

from rest_framework import serializers
from core.classifications.attributes.models.attribute import Attribute
from core.classifications.attributes.models.attribute_option import AttributeOption


class AttributeOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeOption
        fields = [
            "id",
            "code",
            "name",
        ]


class AttributeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = [
            "id",
            "code",
            "name",
            "type",
            "scope",
        ]


class AttributeDetailSerializer(serializers.ModelSerializer):
    options = AttributeOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Attribute
        fields = [
            "id",
            "code",
            "name",
            "type",
            "scope",
            "options",
            "created_at",
            "updated_at",
        ]


class AttributeCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)
    type = serializers.ChoiceField(choices=Attribute.TYPE_CHOICES)
    scope = serializers.CharField(max_length=50)


class AttributeUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    type = serializers.ChoiceField(
        choices=Attribute.TYPE_CHOICES,
        required=False,
    )
    scope = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)


class AttributeOptionCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)


class AttributeOptionUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
