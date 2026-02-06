# business/inventory/views.py

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from business.inventory import selectors
from business.inventory.serializers import (
    WarehouseSerializer,
    StockItemSerializer,
    StockMovementSerializer,
    StockInSerializer,
    StockOutSerializer,
    StockAdjustSerializer,
    InventoryLotSerializer,
    InventoryLotCreateUpdateSerializer,
)
from business.inventory.models.lot import InventoryLot


class WarehouseViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]


    def list(self, request):
        tenant = request.tenant

        warehouses = selectors.get_warehouses(
            tenant=tenant,
            only_active=False
        )

        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        tenant = request.tenant

        warehouse = selectors.get_warehouse_by_id(
            tenant=tenant,
            warehouse_id=pk
        )

        if not warehouse:
            return Response(
                {"detail": "Warehouse not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = WarehouseSerializer(warehouse)
        return Response(serializer.data)


class StockViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]


    def list(self, request):
        tenant = request.tenant
        warehouse_id = request.query_params.get("warehouse_id")

        if not warehouse_id:
            return Response(
                {"detail": "warehouse_id is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        warehouse = selectors.get_warehouse_by_id(
            tenant=tenant,
            warehouse_id=warehouse_id
        )

        if not warehouse:
            return Response(
                {"detail": "Warehouse not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        stock_items = selectors.get_stock_items_by_warehouse(
            tenant=tenant,
            warehouse=warehouse
        )

        serializer = StockItemSerializer(stock_items, many=True)
        return Response(serializer.data)


class StockMovementViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = request.tenant

        product_id = request.query_params.get("product_id")
        warehouse_id = request.query_params.get("warehouse_id")
        reference_type = request.query_params.get("reference_type")
        reference_id = request.query_params.get("reference_id")

        if product_id:
            from business.products.models import Product
            product = Product.objects.filter(
                tenant=tenant,
                id=product_id
            ).first()

            if not product:
                return Response(
                    {"detail": "Product not found."},
                    status=status.HTTP_404_NOT_FOUND
                )

            movements = selectors.get_stock_movements_by_product(
                tenant=tenant,
                product=product
            )

        elif warehouse_id:
            warehouse = selectors.get_warehouse_by_id(
                tenant=tenant,
                warehouse_id=warehouse_id
            )

            if not warehouse:
                return Response(
                    {"detail": "Warehouse not found."},
                    status=status.HTTP_404_NOT_FOUND
                )

            movements = selectors.get_stock_movements_by_warehouse(
                tenant=tenant,
                warehouse=warehouse
            )

        elif reference_type and reference_id:
            movements = selectors.get_stock_movements_by_reference(
                tenant=tenant,
                reference_type=reference_type,
                reference_id=reference_id
            )

        else:
            return Response(
                {"detail": "Invalid query parameters."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = StockMovementSerializer(movements, many=True)
        return Response(serializer.data)


class StockActionViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def stock_in(self, request):
        serializer = StockInSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        movement = serializer.save()

        return Response(
            {"id": movement.id},
            status=status.HTTP_201_CREATED
        )

    def stock_out(self, request):
        serializer = StockOutSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        movement = serializer.save()

        return Response(
            {"id": movement.id},
            status=status.HTTP_201_CREATED
        )

    def adjust(self, request):
        serializer = StockAdjustSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        movement = serializer.save()

        return Response(
            {"id": movement.id},
            status=status.HTTP_201_CREATED
        )


class InventoryLotViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = request.tenant
        product_id = request.query_params.get("product_id")
        warehouse_id = request.query_params.get("warehouse_id")

        lots = selectors.get_inventory_lots(
            tenant=tenant,
            product_id=product_id,
            warehouse_id=warehouse_id
        )

        serializer = InventoryLotSerializer(lots, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tenant = request.tenant

        lot = selectors.get_inventory_lot_by_id(
            tenant=tenant,
            lot_id=pk
        )

        if not lot:
            return Response(
                {"detail": "Lot not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = InventoryLotSerializer(lot)
        return Response(serializer.data)

    def create(self, request):
        serializer = InventoryLotCreateUpdateSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        lot = serializer.save()

        return Response(
            {"id": lot.id},
            status=status.HTTP_201_CREATED
        )
