from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from core.tenants.models import Tenant


class TenantAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if not request.user or not request.user.is_authenticated:
            return None

        tenant_id = getattr(request.auth, "active_tenant", None)
        if not tenant_id:
            raise AuthenticationFailed("Active tenant not set")

        try:
            tenant = Tenant.objects.get(id=tenant_id, is_active=True)
        except Tenant.DoesNotExist:
            raise AuthenticationFailed("Invalid tenant")

        request.tenant = tenant
        return None
