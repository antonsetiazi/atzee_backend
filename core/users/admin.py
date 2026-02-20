# core/users/admin.py


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html

from .models import User
from core.tenants.models import UserTenant


class UserTenantInline(admin.TabularInline):
    model = UserTenant   # ✅ BUKAN Tenant
    extra = 0
    autocomplete_fields = ["tenant"]  # ini field milik UserTenant
    fields = ["tenant", "is_active", "joined_at"]
    readonly_fields = ["joined_at"]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    list_display = (
        "username",
        "email",
        "full_name",
        "is_active",
        "is_verified",
        "primary_tenant",
    )

    list_filter = (
        "is_active",
        "is_verified",
        "is_staff",
        "is_superuser",
    )

    search_fields = (
        "username",
        "email",
        "full_name",
    )

    ordering = ("-date_joined",)

    inlines = [UserTenantInline]

    fieldsets = (
        ("Account", {
            "fields": ("username", "email", "password")
        }),
        ("Profile", {
            "fields": ("full_name", "phone", "avatar")
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_verified",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important Dates", {
            "fields": ("last_login", "date_joined")
        }),
    )

    add_fieldsets = (
        ("Create User", {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "full_name",
                "password1",
                "password2",
                "is_active",
                "is_verified",
            ),
        }),
    )

    readonly_fields = ("last_login", "date_joined")

    def primary_tenant(self, obj):
        membership = obj.tenant_memberships.filter(is_active=True).first()
        if not membership:
            return "-"
        return membership.tenant.code

    primary_tenant.short_description = "Active Tenant"

