# core/roles/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.roles.serializers import (
    RoleSerializer,
    RoleCreateUpdateSerializer
)
from core.roles import services


class RoleListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        roles = services.list_roles(
            tenant=request.tenant
        )
        return Response(RoleSerializer(roles, many=True).data)

    def post(self, request):
        serializer = RoleCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        role = services.create_role(
            tenant=request.tenant,
            data=serializer.validated_data
        )
        return Response(RoleSerializer(role).data, status=201)


class RoleDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, role_id):
        serializer = RoleCreateUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        role = services.update_role(
            tenant=request.tenant,
            role_id=role_id,
            data=serializer.validated_data
        )
        return Response(RoleSerializer(role).data)
