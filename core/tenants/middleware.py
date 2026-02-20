# core/tenants/middleware.py

from django.http import JsonResponse
from core.tenants.models import Tenant

TENANT_OPTIONAL_PATHS = (
    "/api/auth/",
    "/api/tenants",          # list & switch
    "/admin"
)

class TenantContextMiddleware:
    """
    Resolve active tenant from authenticated token context.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Belum login → lewati
        if not request.user.is_authenticated:
            return self.get_response(request)

        # 🔓 BOOTSTRAP API → tenant OPTIONAL
        for path in TENANT_OPTIONAL_PATHS:
            if request.path.startswith(path):
                return self.get_response(request)

        # 🔑 AMBIL DARI HEADER (INI KUNCI)
        tenant_id = request.headers.get("X-Tenant-ID")
        # tenant_id = getattr(request.auth, "active_tenant", None)

        if not tenant_id:
            return JsonResponse(
                {"detail": "Active tenant not set"},
                status=403
            )

        try:
            tenant = Tenant.objects.get(id=tenant_id, is_active=True)
        except Tenant.DoesNotExist:
            return JsonResponse(
                {"detail": "Invalid tenant"},
                status=403
            )

        request.tenant_id = tenant_id
        request.tenant = tenant
        
        return self.get_response(request)
