# core/tenants/middleware.py

from django.http import JsonResponse
from core.tenants.models import Tenant


class TenantContextMiddleware:
    """
    Resolve tenant dari header frontend.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        tenant_code = request.headers.get("X-Tenant-Code")

        if not tenant_code:
            return JsonResponse(
                {"detail": "Tenant code missing"},
                status=400
            )

        try:
            tenant = Tenant.objects.only(
                "id", "name", "code", "branding"
            ).get(
                code=tenant_code,
                is_active=True
            )
        except Tenant.DoesNotExist:
            return JsonResponse(
                {"detail": "Invalid tenant"},
                status=403
            )

        request.tenant = tenant
        request.tenant_id = tenant.id

        return self.get_response(request)