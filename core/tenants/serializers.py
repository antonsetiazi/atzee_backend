# core/tenants/serializers.py

from rest_framework import serializers
from core.tenants.models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    branding = serializers.JSONField()

    class Meta:
        model = Tenant
        fields = ("id", "name", "code", "vertical", "branding")


class TenantSwitchSerializer(serializers.Serializer):
    tenant_id = serializers.UUIDField()
