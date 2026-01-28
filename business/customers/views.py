# business/customers/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from business.customers import selectors, services
from business.customers.serializers import (
    CustomerListSerializer,
    CustomerDetailSerializer,
    CustomerCreateSerializer,
    CustomerUpdateSerializer
)


class CustomerViewSet(viewsets.ViewSet):
    """
    Customer API endpoints (tenant-scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        customers = selectors.get_customers(tenant=tenant)
        serializer = CustomerListSerializer(customers, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        customer = selectors.get_customer_by_id(tenant=tenant, customer_id=pk)

        if not customer:
            return Response(
                {"detail": "Customer not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = CustomerDetailSerializer(customer)
        return Response(serializer.data)
    

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = CustomerCreateSerializer(data=request.data)        
        serializer.is_valid(raise_exception=True)
        customer = services.create_customer(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )
        output = CustomerDetailSerializer(customer)
        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )
    

    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        customer = selectors.get_customer_by_id(tenant=tenant, customer_id=pk)

        if not customer:
            return Response(
                {"detail": "Customer not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = CustomerUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        customer = services.update_customer(
            tenant=tenant,
            customer_id=customer.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = CustomerDetailSerializer(customer)
        return Response(output.data)
    

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_customer(
            tenant=tenant,
            customer_id=pk,
            deleted_by=request.user
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )