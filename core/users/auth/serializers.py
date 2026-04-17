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
    

class MeSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(source="email")
    tenant_id = serializers.SerializerMethodField()
    avatar_url = serializers.SerializerMethodField()
    role_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id", 
            "username", 
            "full_name", 
            "tenant_id",
            "avatar_url",
            "role_id",
        ]

    def get_tenant_id(self, obj):
        membership = obj.tenant_memberships.first()
        if not membership:
            return None
        return str(membership.tenant.id)
    
    def get_avatar_url(self, obj):
        if not obj.avatar:
            return None

        request = self.context.get("request")
        url = obj.avatar.get_download_url()

        if request:
            return request.build_absolute_uri(url)

        return url
    
    def get_role_id(self, obj):
        # Ambil role user di tenant pertama, atau None jika guest
        membership = obj.tenant_memberships.first()
        if not membership:
            return None
        user_role = (
            obj.user_roles.filter(role__tenant_id=membership.tenant.id)
            .select_related("role")
            .first()
        )
        return str(user_role.role.id) if user_role else None
    

class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate_current_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Current password is incorrect")
        return value

    def validate(self, data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError("New passwords do not match")
        validate_password(data["new_password"], user=self.context["request"].user)
        return data
    

class RequestOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)


class VerifyOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)
    otp = serializers.CharField(max_length=128)
    tenant_code = serializers.CharField()    