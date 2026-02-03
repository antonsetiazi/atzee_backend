# core/dashboard/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .registry import DASHBOARD_REGISTRY
from .utils import resolve_service

from django.core.cache import cache
from core.dashboard.cache import dashboard_cache_key
from core.tenants.services import TenantService


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        context = request.query_params.get("context", "default")

        user = request.user
        tenant = TenantService.get_current_tenant(request)

        cache_key = dashboard_cache_key(
            tenant_id=tenant.id,
            context=context,
        )

        cached = cache.get(cache_key)
        if cached:
            return Response(cached)
        
        widgets = DASHBOARD_REGISTRY.get(
            context,
            DASHBOARD_REGISTRY.get("default", [])
        )

        results = []

        for widget in widgets:
            # 🔐 permission check
            if widget.permission and not user.has_perm(widget.permission):
                continue

            service_path = widget.source.get("service")
            params = widget.source.get("params", {})

            service = resolve_service(service_path)

            value = service(
                tenant=tenant,
                user=user,
                **params
            )

            results.append({
                "key": widget.key,
                "type": widget.type,
                "title": widget.title,
                "size": widget.size,
                "value": value,
                "meta": widget.meta,
            })

        response_data = {
            "context": context,
            "available_contexts": list(DASHBOARD_REGISTRY.keys()),
            "widgets": results
        }

        # ⏱ cache 2 menit (contoh)
        cache.set(cache_key, response_data, timeout=120)

        return Response(response_data)
