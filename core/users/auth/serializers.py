from rest_framework import serializers
from django.contrib.auth import authenticate
from core.tenants.models import Tenant
from core.users.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    tenant_code = serializers.CharField()

    def validate(self, data):
        try:
            tenant = Tenant.objects.get(
                code=data["tenant_code"],
                is_active=True
            )
        except Tenant.DoesNotExist:
            raise serializers.ValidationError("Invalid tenant")

        try:
            user = User.objects.get(username=data["username"])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        if not user.check_password(data["password"]):
            raise serializers.ValidationError("Invalid credentials")

        if not user.is_active:
            raise serializers.ValidationError("User inactive")

        if not user.tenant_memberships.filter(
            tenant=tenant,
            is_active=True
        ).exists():
            raise serializers.ValidationError(
                "User not member of this tenant"
            )
        
        data["user"] = user
        data["tenant"] = tenant
        return data
