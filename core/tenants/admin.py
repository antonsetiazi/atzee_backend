from django.contrib import admin
from .models import Tenant, UserTenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "is_active")


@admin.register(UserTenant)
class UserTenantAdmin(admin.ModelAdmin):
    list_display = ("user", "tenant", "is_active", "joined_at")
    list_filter = ("is_active", "tenant")
