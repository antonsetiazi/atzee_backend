# business/users/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from core.tenants.services import TenantService
from business.users import selectors, services
from business.users.serializers import (
    BusinessUserListSerializer,
    BusinessUserDetailSerializer,
    BusinessUserCreateSerializer,
    BusinessUserUpdateSerializer,
)


class BusinessUserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        users = selectors.get_users(tenant=tenant)
        serializer = BusinessUserListSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        user = selectors.get_user_by_id(tenant=tenant, user_id=pk)

        if not user:
            return Response(
                {"detail": "Business user not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BusinessUserDetailSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = BusinessUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = services.create_business_user(
            tenant=tenant,
            core_user=request.user,
            created_by=request.user,
            **serializer.validated_data
        )

        output = BusinessUserDetailSerializer(user)
        return Response(output.data, status=status.HTTP_201_CREATED)


    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        user = selectors.get_user_by_id(
            tenant=tenant,
            user_id=pk
        )

        if not user:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BusinessUserUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        user = services.update_business_user(
            tenant=tenant,
            user_id=user.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = BusinessUserDetailSerializer(user)
        return Response(output.data)
    

    @action(detail=False, methods=["get", "patch"], url_path="me")
    def me(self, request):
        tenant = TenantService.get_current_tenant(request)

        user = selectors.get_user_by_core_user(
            tenant=tenant,
            core_user_id=request.user.id,
        )

        if not user:
            return Response(
                {"detail": "Profile not found."},
                status=404
            )

        if request.method == "GET":
            serializer = BusinessUserDetailSerializer(user)
            return Response(serializer.data)

        # PATCH
        updated = services.update_business_user(
            tenant=tenant,
            user_id=user.id,
            updated_by=request.user,
            **request.data
        )

        serializer = BusinessUserDetailSerializer(updated)
        return Response(serializer.data)