# accounting/services/fixed_asset_service.py

from decimal import Decimal

from django.db import transaction

from accounting.models import (
    AssetCategory,
    FixedAsset,
)
from core.activity.constants.activity_types import FIXED_ASSET
from core.activity.events.finance_events import FinanceEvents
from core.activity.services.activity_service import ActivityService


class FixedAssetService:

    # =========================================================
    # CREATE FIXED ASSET
    # =========================================================
    @staticmethod
    @transaction.atomic
    def create_asset(
        *,
        tenant,
        user,
        asset_number,
        name,
        serial_number,
        location,
        category_id,
        purchase_date,
        capitalization_date,
        purchase_cost,
        depreciation_start_date,
        description="",
        salvage_value=None,
    ):
        category = AssetCategory.objects.get(
            id=category_id,
            tenant=tenant,
            is_deleted=False,
        )

        purchase_cost = Decimal(str(purchase_cost))

        # =====================================================
        # AUTO SALVAGE VALUE
        # =====================================================
        if salvage_value is None:

            salvage_value = (
                purchase_cost * category.salvage_value_percent / Decimal("100")
            )

        salvage_value = Decimal(str(salvage_value))

        # =====================================================
        # INITIAL BOOK VALUE
        # =====================================================
        initial_book_value = purchase_cost - salvage_value

        # =====================================================
        # CREATE ASSET
        # =====================================================
        asset = FixedAsset.objects.create(
            tenant=tenant,
            asset_number=asset_number,
            name=name,
            description=description,
            category=category,
            serial_number=serial_number,
            location=location,
            purchase_date=purchase_date,
            capitalization_date=capitalization_date,
            purchase_cost=purchase_cost,
            salvage_value=salvage_value,
            depreciation_method=(category.depreciation_method),
            useful_life_months=(category.useful_life_months),
            depreciation_start_date=(depreciation_start_date),
            accumulated_depreciation=Decimal("0"),
            book_value=initial_book_value,
            status="draft",
            created_by=user,
        )

        # =====================================================
        # RECORD ACTIVITY
        # =====================================================
        ActivityService.record(
            tenant=tenant,
            target_type=FIXED_ASSET,
            target_id=asset.id,
            event=FinanceEvents.FIXED_ASSET_CREATED,
            title="Fixed asset created",
            description=(f"Asset '{asset.name}' has been registered"),
            created_by=user,
            metadata={
                "asset_number": asset.asset_number,
                "category": category.name,
                "purchase_cost": str(asset.purchase_cost),
                "salvage_value": str(asset.salvage_value),
                "book_value": str(asset.book_value),
                "depreciation_method": (asset.depreciation_method),
                "useful_life_months": (asset.useful_life_months),
            },
        )

        return asset

    # =========================================================
    # ACTIVATE ASSET
    # =========================================================
    @staticmethod
    @transaction.atomic
    def activate_asset(*, asset, user):

        if asset.status != "draft":
            raise ValueError("Only draft asset can be activated")

        asset.status = "active"
        asset.updated_by = user
        asset.save()

        # =====================================================
        # RECORD ACTIVITY
        # =====================================================
        ActivityService.record(
            tenant=asset.tenant,
            target_type=FIXED_ASSET,
            target_id=asset.id,
            event=FinanceEvents.FIXED_ASSET_ACTIVATED,
            title="Fixed asset activated",
            description=(f"Asset '{asset.name}' is now active"),
            created_by=user,
            metadata={
                "asset_number": asset.asset_number,
                "status": asset.status,
            },
        )

        return asset

    # =========================================================
    # UPDATE FIXED ASSET
    # =========================================================
    @staticmethod
    @transaction.atomic
    def update_asset(
        *,
        asset,
        user,
        data,
    ):

        old_values = {
            "name": asset.name,
            "location": asset.location,
            "description": asset.description,
            "serial_number": asset.serial_number,
        }

        for field, value in data.items():
            setattr(asset, field, value)

        asset.updated_by = user
        asset.save()

        # =====================================================
        # RECORD ACTIVITY
        # =====================================================
        ActivityService.record(
            tenant=asset.tenant,
            target_type=FIXED_ASSET,
            target_id=asset.id,
            event=FinanceEvents.FIXED_ASSET_UPDATED,
            title="Fixed asset updated",
            description=(f"Asset '{asset.name}' has been updated"),
            created_by=user,
            metadata={
                "before": old_values,
                "updated_fields": list(data.keys()),
            },
        )

        return asset
