# business/payment_gateway/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from business.payment_gateway.models import PaymentMethod, PaymentGatewayConfig
from business.payment_gateway.serializers import (
    PaymentMethodSerializer,
    PaymentGatewayConfigSerializer,
    PaymentMethodPublicSerializer
)
from business.payment_gateway import selectors
from business.payment_gateway.services.config_service import (
    upsert_gateway_config
)


# ------------------------------
# PAYMENT METHOD
# ------------------------------

class PaymentMethodViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        methods = selectors.get_payment_methods(tenant=request.tenant)

        methods = methods.filter(is_active=True)

        serializer = PaymentMethodPublicSerializer(methods, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PaymentMethodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        method = serializer.save(tenant=request.tenant)
        return Response(
            PaymentMethodSerializer(method).data,
            status=status.HTTP_201_CREATED
        )

    def partial_update(self, request, pk=None):
        method = PaymentMethod.objects.get(id=pk, tenant=request.tenant)

        serializer = PaymentMethodSerializer(
            method,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        method = PaymentMethod.objects.get(id=pk, tenant=request.tenant)
        method.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------------
# GATEWAY CONFIG
# ------------------------------

class PaymentGatewayConfigViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        configs = selectors.get_gateway_configs(tenant=request.tenant)
        serializer = PaymentGatewayConfigSerializer(configs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PaymentGatewayConfigSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        config = upsert_gateway_config(
            tenant=request.tenant,
            **serializer.validated_data
        )

        return Response(
            PaymentGatewayConfigSerializer(config).data,
            status=status.HTTP_201_CREATED
        )
    