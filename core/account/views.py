# core/account/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.views import APIView

from core.users.auth.services import update_user_profile
from core.account.serializers import UserSettingsSerializer
from core.tenants.services import TenantService
from core.account import selectors, services
from core.account.serializers import (
    UserAddressListSerializer,
    UserAddressDetailSerializer,
    UserAddressCreateSerializer,
    UserAddressUpdateSerializer,
    UserBankSerializer,
    UserBankCreateSerializer,
    UserBankUpdateSerializer
)

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = update_user_profile(
            user=request.user,
            data=request.data
        )

        return Response({
            "full_name": user.full_name,
            "phone": user.phone,
        })
    

class UserSettingsView(RetrieveUpdateAPIView):
    serializer_class = UserSettingsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.settings


class UserAddressViewSet(viewsets.ViewSet):
    """
    User Address API endpoints (tenant-scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)

        addresses = selectors.get_user_addresses(
            tenant=tenant,
            user=request.user
        )

        serializer = UserAddressListSerializer(addresses, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        address = selectors.get_user_address_by_id(
            tenant=tenant,
            user=request.user,
            address_id=pk
        )

        if not address:
            return Response(
                {"detail": "Address not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserAddressDetailSerializer(address)
        return Response(serializer.data)


    def create(self, request):
        try:
            tenant = TenantService.get_current_tenant(request)

            serializer = UserAddressCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            address = services.create_user_address(
                tenant=tenant,
                user=request.user,
                **serializer.validated_data
            )

            output = UserAddressDetailSerializer(address)

            return Response(
                output.data,
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(e)


    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = UserAddressUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        address = services.update_user_address(
            tenant=tenant,
            user=request.user,
            address_id=pk,
            **serializer.validated_data
        )

        output = UserAddressDetailSerializer(address)
        return Response(output.data)


    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = UserAddressUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        address = services.update_user_address(
            tenant=tenant,
            user=request.user,
            address_id=pk,
            **serializer.validated_data
        )

        output = UserAddressDetailSerializer(address)
        return Response(output.data)
    

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_user_address(
            tenant=tenant,
            user=request.user,
            address_id=pk
        )

        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=True, methods=["post"])
    def set_default(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        address = services.set_default_address(
            tenant=tenant,
            user=request.user,
            address_id=pk
        )

        serializer = UserAddressDetailSerializer(address)
        return Response(serializer.data)
    

class UserBankViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)

        banks = selectors.get_user_banks(
            tenant=tenant,
            user=request.user
        )

        serializer = UserBankSerializer(banks, many=True)
        return Response(serializer.data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = UserBankCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        bank = services.create_user_bank(
            tenant=tenant,
            user=request.user,
            **serializer.validated_data
        )

        return Response(UserBankSerializer(bank).data)

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = UserBankUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        bank = services.update_user_bank(
            tenant=tenant,
            user=request.user,
            bank_id=pk,
            **serializer.validated_data
        )

        return Response(UserBankSerializer(bank).data)

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_user_bank(
            tenant=tenant,
            user=request.user,
            bank_id=pk
        )

        return Response(status=204)

    @action(detail=True, methods=["post"])
    def set_default(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        bank = services.set_default_bank(
            tenant=tenant,
            user=request.user,
            bank_id=pk
        )

        return Response(UserBankSerializer(bank).data)    