# core/tenants/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from core.tenants.serializers import (
    TenantSerializer,
    TenantSwitchSerializer,
)
from core.tenants.services import (
    get_user_tenants,
    validate_user_tenant_access
)
from core.roles.services import ensure_user_has_role
from core.roles.services import ensure_user_is_admin

from core.users.auth.services import issue_jwt_for_user

from core.permissions.bootstrap import sync_permissions_from_ui
from core.roles.bootstrap import (
    ensure_admin_role,
    assign_all_permissions_to_role,
)

# GET /api/tenants
class TenantListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenants = get_user_tenants(request.user)
        serializer = TenantSerializer(tenants, many=True)
        return Response(serializer.data)


# GET /api/tenants/current
class CurrentTenantView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        tenant = getattr(request, "tenant", None)

        if not tenant:
            return Response(
                {"detail": "Tenant not resolved"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = TenantSerializer(tenant)
        return Response(serializer.data)


# POST /api/tenants/switch
# class TenantSwitchView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = TenantSwitchSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         tenant_id = serializer.validated_data["tenant_id"]

#         tenant = validate_user_tenant_access(
#             user=request.user,
#             tenant_id=tenant_id,
#         )

#         # 🔥 BOOTSTRAP STEP 1: sync permissions
#         sync_permissions_from_ui(tenant=tenant)

#         # 🔥 BOOTSTRAP STEP 2: ensure admin role
#         admin_role = ensure_admin_role(tenant=tenant)

#         # 🔥 BOOTSTRAP STEP 3: assign all permissions to admin
#         assign_all_permissions_to_role(role=admin_role)

#         # 🔥 BOOTSTRAP STEP 4: pastikan user punya role
#         ensure_user_has_role(
#             user=request.user,
#             tenant=tenant,
#         )

#         ensure_user_is_admin(
#             user=request.user,
#             tenant=tenant,
#         )

#         tokens = issue_jwt_for_user(
#             user=request.user,
#             active_tenant_id=str(tenant.id),
#         )

#         return Response(tokens, status=status.HTTP_200_OK)
