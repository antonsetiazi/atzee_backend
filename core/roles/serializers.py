# core/roles/serializers.py

from rest_framework import serializers
from core.roles.models import Role
from core.roles.enums import RoleCode


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            "id",
            "code",
            "name",
            "description",
            "access_level",
        ]


class RoleCreateUpdateSerializer(serializers.ModelSerializer):
    code = serializers.ChoiceField(
        choices=[r.value for r in RoleCode]
    )

    class Meta:
        model = Role
        fields = [
            "code",
            "name",
            "description",
            "access_level",
        ]
