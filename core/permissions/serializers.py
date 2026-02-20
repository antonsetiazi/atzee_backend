# core/permissions/serializers.py

from rest_framework import serializers
from core.permissions.models import Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ["module", "code", "description"]
