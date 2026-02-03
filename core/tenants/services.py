# core/tenants/services.py

from core.tenants.models import Tenant, UserTenant
from django.core.exceptions import PermissionDenied


class TenantService:
    """
    Single source of truth untuk tenant context
    """

    @staticmethod
    def get_user_tenants(user):
        return Tenant.objects.filter(
            user_memberships__user=user,
            user_memberships__is_active=True,
            is_active=True,
        ).distinct()

    @staticmethod
    def validate_user_tenant_access(user, tenant_id):
        exists = UserTenant.objects.filter(
            user=user,
            tenant_id=tenant_id,
            is_active=True,
            tenant__is_active=True,
        ).exists()

        if not exists:
            raise PermissionDenied("User has no access to this tenant")

        return Tenant.objects.get(id=tenant_id)

    @staticmethod
    def get_current_tenant(request):
        """
        Resolve tenant dari request (header / token)
        """
        tenant_id = request.META.get("HTTP_X_TENANT_ID") 

        if not tenant_id:
            raise PermissionDenied("Tenant context missing")

        return TenantService.validate_user_tenant_access(
            user=request.user,
            tenant_id=tenant_id,
        )


# ------------------------------------------------------------------
# BACKWARD COMPATIBILITY (optional tapi aman)
# ------------------------------------------------------------------

def get_user_tenants(user):
    return TenantService.get_user_tenants(user)


def validate_user_tenant_access(user, tenant_id):
    return TenantService.validate_user_tenant_access(user, tenant_id)
