# core/entities/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from .services import EntityQueryService


class EntityQueryView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, entity_key):
        # print("EntityQueryView | post")
        tenant = TenantService.get_current_tenant(request)

        try:
            result = EntityQueryService.execute(
                user=request.user,
                tenant=tenant,
                entity_key=entity_key,
                query=request.data or {},
            )
        except PermissionError:
            return Response({"detail": "Forbidden"}, status=403)
        except ValueError as e:
            return Response({"detail": str(e)}, status=404)
        except Exception:
            return Response(
                {"detail": "Internal server error"},
                status=500,
            )

        return Response(result)
