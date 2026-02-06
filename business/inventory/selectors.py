# business/inventory/selectors.py
from decimal import Decimal
from typing import Optional
from django.db import models
from django.db.models import QuerySet, Q, Sum

from core.tenants.models import Tenant

from business.inventory.models.warehouse import Warehouse
from business.inventory.models.stock_item import StockItem
from business.inventory.models.stock_movement import StockMovement
from business.inventory.models.lot import InventoryLot
from business.products.models import Product


def get_warehouses(
        *,
        tenant: Tenant,
        only_active: bool = True
) -> QuerySet[Warehouse]:
    qs = Warehouse.objects.filter(
        tenant=tenant,
        is_deleted=False
    )

    if only_active:
        qs = qs.filter(is_active=True)

    return qs.order_by("name")


def get_warehouse_by_id(
        *,
        tenant: Tenant,
        warehouse_id: int
) -> Optional[Warehouse]:
    try:
        return Warehouse.objects.get(
            tenant=tenant,
            id=warehouse_id,
            is_deleted=False
        )
    except Warehouse.DoesNotExist:
        return None
    

def get_stock_items_queryset(
        *,
        tenant: Tenant
) -> QuerySet[StockItem]:
    return StockItem.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_stock_item(
        *,
        tenant: Tenant,
        product: Product,
        warehouse: Warehouse
) -> Optional[StockItem]:
    try:
        return get_stock_items_queryset(tenant=tenant).get(
            product=product,
            warehouse=warehouse
        )
    except StockItem.DoesNotExist:
        return None
    

def get_stock_items_by_warehouse(
        *,
        tenant: Tenant,
        warehouse: Warehouse
) -> QuerySet[StockItem]:
    return (
        get_stock_items_queryset(tenant=tenant)
        .filter(warehouse=warehouse)
        .select_related("product")
        .order_by("product__name")
    )


def get_stock_movement_queryset(
        *, 
        tenant: Tenant
) -> QuerySet[StockMovement]:
    return StockMovement.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_stock_movements_by_product(
        *,
        tenant: Tenant,
        product: Product
) -> QuerySet[StockMovement]:
    return (
        get_stock_movement_queryset(tenant=tenant)
        .filter(product=product)
        .select_related("warehouse")
        .order_by("-created_at")
    )


def get_stock_movements_by_warehouse(
        *, 
        tenant: Tenant,
        warehouse: Warehouse
) -> QuerySet[StockMovement]:
    return (
        get_stock_movement_queryset(tenant=tenant)
        .filter(warehouse=warehouse)
        .select_related("product")
        .order_by("-created_at")
    )


def get_stock_movements_by_reference(
        *,
        tenant: Tenant,
        reference_type: str,
        reference_id: int
) -> QuerySet[StockMovement]:
    return (
        get_stock_movement_queryset(tenant=tenant)
        .filter(
            reference_type=reference_type,
            reference_id=reference_id
        )
        .select_related("product", "warehouse")
        .order_by("created_at")
    )


def get_total_stock_for_product(
        *,
        tenant: Tenant,
        product: Product
) -> float:
    result = get_stock_items_queryset(tenant=tenant).filter(
        product=product
    ).aggregate(total=Sum("quantity"))

    return result["total"] or 0


def warehouse_exists(
        *, 
        tenant: Tenant,
        warehouse_id: int
) -> bool:
    return Warehouse.objects.filter(
        tenant=tenant,
        id=warehouse_id,
        is_deleted=False
    ).exists()


def get_lots_by_product(
    *,
    tenant: Tenant,
    product: Product,
    warehouse: Warehouse | None = None
):
    qs = InventoryLot.objects.filter(
        tenant=tenant,
        product=product,
        is_active=True,
        is_deleted=False
    )

    return qs


def get_available_qty_by_lot(
    *,
    tenant: Tenant,
    lot: InventoryLot,
    warehouse: Warehouse | None = None
):
    qs = StockMovement.objects.filter(
        tenant=tenant,
        lot=lot,
        is_deleted=False
    )

    if warehouse:
        qs = qs.filter(warehouse=warehouse)

    result = qs.aggregate(
        total=Sum(
            models.Case(
                models.When(
                    movement_type=StockMovement.IN,
                    then="quantity"
                ),
                models.When(
                    movement_type=StockMovement.OUT,
                    then=-models.F("quantity")
                ),
                default=0,
                output_field=models.DecimalField(),
            )
        )
    )

    return result["total"] or Decimal("0")


def get_available_lots_fefo(
    *,
    tenant: Tenant,
    product: Product,
    warehouse: Warehouse
) -> QuerySet[InventoryLot]:
    """
    Return available lots ordered by FEFO (earliest expiry first).
    """
    return (
        InventoryLot.objects
        .filter(
            tenant=tenant,
            product=product,
            warehouse=warehouse,
            quantity__gt=0,
            is_deleted=False,
        )
        .order_by("expiry_date", "created_at")
    )


def get_inventory_lots(
    *,
    tenant: Tenant,
    product_id: int | None = None,
    warehouse_id: int | None = None
):
    qs = InventoryLot.objects.filter(
        tenant=tenant,
        is_deleted=False
    )

    if product_id:
        qs = qs.filter(product_id=product_id)

    if warehouse_id:
        qs = qs.filter(warehouse_id=warehouse_id)

    return qs.select_related(
        "product",
        "warehouse"
    ).order_by("expiry_date", "created_at")


def get_inventory_lot_by_id(
    *,
    tenant: Tenant,
    lot_id: int
) -> InventoryLot | None:
    try:
        return InventoryLot.objects.get(
            tenant=tenant,
            id=lot_id,
            is_deleted=False
        )
    except InventoryLot.DoesNotExist:
        return None
