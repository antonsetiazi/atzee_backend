# business/inventory/services.py

from decimal import Decimal

from django.db import transaction
from django.core.exceptions import ValidationError

from core.tenants.models import Tenant
from core.users.models import User
from business.products.models import Product
from business.inventory.models.warehouse import Warehouse
from business.inventory.models.stock_item import StockItem
from business.inventory.models.stock_movement import StockMovement
from business.inventory.models.lot import InventoryLot
from business.inventory import selectors


def _validate_lot_requirement(
    *,
    product: Product,
    lot: InventoryLot | None
) -> None:
    """
    Validate lot requirement based on product tracking type.
    This is a business invariant, not UI concern.
    """
    if lot and lot.product_id != product.id:
        raise ValidationError("Lot does not belong to this product.")
    

def _consume_lot_quantity(
    *,
    lot: InventoryLot,
    quantity: Decimal,
    user: User
) -> None:
    if lot.quantity < quantity:
        raise ValidationError("Lot has insufficient quantity.")

    lot.quantity -= quantity
    lot.updated_by = user
    lot.save(update_fields=["quantity", "updated_by", "updated_at"])


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
    lot: InventoryLot | None = None,
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

    if lot:
        lot.quantity += quantity
        lot.updated_by = user
        lot.save(update_fields=["quantity", "updated_by", "updated_at"])

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
    stock_item.updated_by = user
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
    lot: InventoryLot | None = None,
    reference_type: str = "",
    reference_id: int | None = None,
    note: str = ""
) -> StockMovement:
    if quantity <= 0:
        raise ValidationError("Quantity must be greater than zero.")
    
    # 🔒 Lot enforcement
    _validate_lot_requirement(product=product, lot=lot)

    stock_item = selectors.get_stock_item(
        tenant=tenant,
        product=product,
        warehouse=warehouse
    )

    if not stock_item or stock_item.quantity < quantity:
        raise ValidationError("Insufficient stock.")

    # =========================
    # LOT TRACKING
    # =========================
    if product.tracking_type == "lot":

        # 🔹 MANUAL LOT MODE
        if lot:
            _consume_lot_quantity(
                lot=lot,
                quantity=quantity,
                user=user
            )

        # 🔹 FEFO MODE
        else:
            remaining = quantity

            lots = selectors.get_available_lots_fefo(
                tenant=tenant,
                product=product,
                warehouse=warehouse
            )

            for lot_obj in lots:
                if remaining <= 0:
                    break

                consume_qty = min(lot_obj.quantity, remaining)

                _consume_lot_quantity(
                    lot=lot_obj,
                    quantity=consume_qty,
                    user=user
                )

                remaining -= consume_qty

            if remaining > 0:
                raise ValidationError("Insufficient lot stock.")
            
    # =========================
    # MOVEMENT RECORD
    # =========================
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
    lot: InventoryLot | None = None,
    note: str = ""
) -> StockMovement:
    if new_quantity < 0:
        raise ValidationError("Quantity cannot be negative.")
    
    _validate_lot_requirement(product=product, lot=lot)

    stock_item = _get_or_create_stock_item(
        tenant=tenant,
        product=product,
        warehouse=warehouse,
        user=user
    )

    current_quantity = lot.quantity if lot else stock_item.quantity
    difference = new_quantity - stock_item.quantity

    if difference == 0:
        raise ValidationError("No stock difference to adjust")
    
    movement_type = (
        StockMovement.IN if difference > 0 else StockMovement.OUT
    )

    if lot:
        lot.quantity = new_quantity
        lot.updated_by = user
        lot.save(update_fields=["quantity", "updated_by", "updated_at"])

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