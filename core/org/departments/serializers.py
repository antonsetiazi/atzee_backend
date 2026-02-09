# core/org/departments/serializers.py

from rest_framework import serializers
from core.org.departments.models import Department


class DepartmentListSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = [
            "id",
            "code",
            "name",
            "parent",
        ]

    def get_parent(self, obj):
        if not obj.parent:
            return None
        return {
            "id": obj.parent.id,
            "name": obj.parent.name,
        }


class DepartmentDetailSerializer(serializers.ModelSerializer):
    parent_id = serializers.IntegerField(
        source="parent.id",
        allow_null=True,
        required=False
    )

    class Meta:
        model = Department
        fields = [
            "id",
            "code",
            "name",
            "description",
            "parent_id",
            "created_at",
            "updated_at",
        ]


class DepartmentCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=False,)
    parent_id = serializers.IntegerField(required=False, allow_null=True)


class DepartmentUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False, allow_blank=True)
    parent_id = serializers.IntegerField(required=False, allow_null=True)
    is_active = serializers.BooleanField(required=False)
