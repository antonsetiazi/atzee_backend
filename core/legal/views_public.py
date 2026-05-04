# core/legal/views_public.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.legal import selectors


@api_view(["GET"])
@permission_classes([AllowAny])
def get_latest_policy(request):
    tenant = TenantService.get_current_tenant(request)

    policy_type = request.query_params.get("type")

    if not policy_type:
        return Response({"error": "type is required"}, status=400)

    policy = selectors.get_latest_policy(
        tenant=tenant,
        policy_type=policy_type,
    )

    if not policy:
        return Response({"error": "policy not found"}, status=404)

    return Response({
        "title": policy.title,
        "content": policy.content,
        "version": policy.version,
        "updated_at": policy.updated_at,
    })