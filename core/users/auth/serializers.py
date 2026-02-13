# core/users/auth/serializers.py

from rest_framework import serializers
from django.contrib.auth import authenticate
from django.conf import settings
from core.tenants.models import Tenant
from core.users.models import User
from django.contrib.auth.password_validation import validate_password


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
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
            user = User.objects.get(email__iexact=data["email"])
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


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    full_name = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    tenant_code = serializers.CharField()


    class Meta:
        model = User
        fields = ["email", "full_name", "password", "tenant_code"]


    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already registered")
        return value


    def validate_password(self, value):
        validate_password(value)
        return value
    

    def validate_tenant_code(self, value):
        try:
            tenant = Tenant.objects.get(code=value, is_active=True)
        except Tenant.DoesNotExist:
            raise serializers.ValidationError("Invalid tenant")
        return tenant


    def create(self, validated_data):
        tenant = validated_data.pop("tenant_code") 

        user = User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            full_name=validated_data["full_name"],
            password=validated_data["password"],
        )

        # assign user to tenant
        user.tenant_memberships.create(tenant=tenant, is_active=True)

        return user