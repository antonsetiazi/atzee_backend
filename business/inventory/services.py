from decimal import Decimal

from django.db import transaction
from django.core.exceptions import ValidationError

from core.tenants.models import Tenant
from core.users.models import User
from business.products.models import Product
from business.inventory.models import (
    Warehouse,
    StockItem,
    StockMovement
)
from business.inventory import selectors


def _get_or_create_stock_item(
        *,
        tenant: Tenant,
        product: Product,
        warehouse: Warehouse,
        user: User
) -> StockItem:
    stock_item, created = StockItem.objects.get_or_create(
        tenant=tenant,
        product=product,
        warehouse=warehouse,
        defaults={
            "quantity": Decimal("0"),
            "created_by": user,
            "updated_by": user
        }
    )

    if not created:
        stock_item.updated_by = user

    return stock_item


@transaction.atomic
def stock_in(
    *,
    tenant: Tenant,
    user: User,
    product: Product,
    warehouse: Warehouse,
    quantity: Decimal,
    reference_type: str = "",
    reference_id: int | None = None,
    note: str = ""
) -> StockMovement:
    if quantity <= 0:
        raise ValidationError("Quantity must be greater than zero.")
    
    stock_item = _get_or_create_stock_item(
        tenant=tenant,
        product=product,
        warehouse=warehouse,
        user=user
    )

    movement = StockMovement.objects.create(
        tenant=tenant,
        product=product,
        warehouse=warehouse,
        movement_type=StockMovement.IN,
        quantity=quantity,
        reference_type=reference_type,
        reference_id=reference_id,
        note=note,
        created_by=user,
        updated_by=user,
    )

    stock_item.quantity += quantity
    stock_item.save(update_fields=["quantity", "updated_by", "updated_at"])

    return movement


@transaction.atomic
def stock_out(
    *,
    tenant: Tenant,
    user: User,
    product: Product,
    warehouse: Warehouse,
    quantity: Decimal,
    reference_type: str = "",
    reference_id: int | None = None,
    note: str = ""
) -> StockMovement:
    if quantity <= 0:
        raise ValidationError("Quantity must be greater than zero.")
    
    stock_item = selectors.get_stock_item(
        tenant=tenant,
        product=product,
        warehouse=warehouse
    )

    if not stock_item or stock_item.quantity < quantity:
        raise ValidationError("Insufficient stock.")

    movement = StockMovement.objects.create(
        tenant=tenant,
        product=product,
        warehouse=warehouse,
        movement_type=StockMovement.OUT,
        quantity=quantity,
        reference_type=reference_type,
        reference_id=reference_id,
        note=note,
        created_by=user,
        updated_by=user,
    )

    stock_item.quantity -= quantity
    stock_item.updated_by = user
    stock_item.save(update_fields=["quantity", "updated_by", "updated_at"])

    return movement


@transaction.atomic
def stock_adjust(
    *,
    tenant: Tenant,
    user: User,
    product: Product,
    warehouse: Warehouse,
    new_quantity: Decimal,
    note: str = ""
) -> StockMovement:
    if new_quantity < 0:
        raise ValidationError("Quantity cannot be negative.")
    
    stock_item = _get_or_create_stock_item(
        tenant=tenant,
        product=product,
        warehouse=warehouse,
        user=user
    )

    difference = new_quantity - stock_item.quantity

    if difference == 0:
        raise ValidationError("No stock difference to adjust")
    
    movement_type = (
        StockMovement.IN if difference > 0 else StockMovement.OUT
    )

    movement = StockMovement.objects.create(
        tenant=tenant,
        product=product,
        warehouse=warehouse,
        movement_type=movement_type,
        quantity=abs(difference),
        reference_type="ADJUSTMENT",
        note=note,
        created_by=user,
        updated_by=user,
    )

    stock_item.quantity = new_quantity
    stock_item.updated_by = user
    stock_item.save(update_fields=["quantity", "updated_by", "updated_at"])

    return movement