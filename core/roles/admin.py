# core/roles/admin.py

from django.contrib import admin
from core.roles.models import Role, UserRole

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tenant",
        "code",
        "name",
        "access_level",
        "is_system",
    )
    list_filter = ("tenant", "code")
    search_fields = ("name",)


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "role",
        "assigned_at",
    )
