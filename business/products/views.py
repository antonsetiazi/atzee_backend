# business/products/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from business.products import selectors, services
from business.products.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    ProductCreateSerializer,
    ProductUpdateSerializer
)


class ProductViewSet(viewsets.ViewSet):
    """
    Product API endpoints (tenant-scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        products = selectors.get_products(tenant=tenant)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        product = selectors.get_product_by_id(tenant=tenant, product_id=pk)

        if not product:
            return Response(
                {"detail": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
    

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = services.create_product(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        output = ProductDetailSerializer(product)

        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )
    

    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        product = selectors.get_product_by_id(tenant=tenant, product_id=pk)

        if not product:
            return Response(
                {"detail": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        product = services.update_product(
            tenant=tenant,
            product_id=product.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = ProductDetailSerializer(product)
        return Response(output.data)
    

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        product = selectors.get_product_by_id(tenant=tenant, product_id=pk)

        if not product:
            return Response(
                {"detail": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        product = services.update_product(
            tenant=tenant,
            product_id=product.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = ProductDetailSerializer(product)
        return Response(output.data)
    

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        product = selectors.get_product_by_id(tenant=tenant, product_id=pk)

        if not product:
            return Response(
                {"detail": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        services.delete_product(
            tenant=tenant,
            product_id=pk,
            deleted_by=request.user
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )