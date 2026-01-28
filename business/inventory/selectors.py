from typing import Optional
from django.db.models import QuerySet, Q, Sum

from core.tenants.models import Tenant
from business.inventory.models import (
    Warehouse,
    StockItem,
    StockMovement
)
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