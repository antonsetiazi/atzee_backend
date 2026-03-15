# core/permissions/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.permissions.models import Permission
from core.permissions.serializers import PermissionSerializer
from core.permissions.services import PermissionService
from core.tenants.services import TenantService

class MyPermissionView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)
        
        # GUEST
        if not request.user.is_authenticated:
            permissions = Permission.objects.filter(
                tenant=tenant,
                permission_roles__role__code="guest"
            ).values_list("code", flat=True)

            return Response(list(permissions))
        

        # AUTHENTICATED USER
        permissions = Permission.objects.filter(
            tenant=tenant,
            permission_roles__role__role_users__user=request.user
        ).values_list("code", flat=True).distinct()

        return Response(list(permissions))


class PermissionCheckView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        permission_code = request.data.get("permission")

        allowed = PermissionService.can_access(
            user=request.user,
            tenant=request.tenant,
            permission_code=permission_code
        )

        return Response({
            "permission": permission_code,
            "allowed": allowed
        })
