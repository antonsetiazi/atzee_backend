# core/entities/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from .services import EntityQueryService
from .services import EntityExecuteService


class EntityQueryView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, domain: str, entity: str):
        # print('post')
        # print(domain)
        # print(entity)
        if not domain or not entity:
            return Response(
                {"detail": "Invalid entity route"},
                status=400,
            )
        # print('1')
        tenant = TenantService.get_current_tenant(request)
        # print('2')
                
        try:
            result = EntityQueryService.execute(
                user=request.user,
                tenant=tenant,
                domain=domain,
                entity_key=entity,
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


class EntityExecuteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, domain: str, entity: str):

        if not domain or not entity:
            return Response({"detail": "Invalid entity route"}, status=400)

        tenant = TenantService.get_current_tenant(request)

        try:
            result = EntityExecuteService.execute(
                user=request.user,
                tenant=tenant,
                domain=domain,
                entity_key=entity,
                data=request.data or {},
            )
        except PermissionError:
            return Response({"detail": "Forbidden"}, status=403)
        except ValueError as e:
            return Response({"detail": str(e)}, status=404)
        except Exception as e:
            print("Entity execute error:", e)
            return Response({"detail": "Internal server error"}, status=500)

        return Response(result)