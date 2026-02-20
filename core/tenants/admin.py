# core/tenants/admin.py

from django.contrib import admin
from .models import Tenant, UserTenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "vertical", "is_active")
    list_filter = ("vertical", "is_active")
    search_fields = ("name", "code")

    def get_readonly_fields(self, request, obj=None):
        if obj:  # jika sudah ada
            return ("vertical",)
        return ()


@admin.register(UserTenant)
class UserTenantAdmin(admin.ModelAdmin):
    list_display = ("user", "tenant", "is_active", "joined_at")
    list_filter = ("is_active", "tenant")
