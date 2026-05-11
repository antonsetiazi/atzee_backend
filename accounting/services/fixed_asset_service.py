# accounting/services/fixed_asset_service.py

from decimal import Decimal

from django.db import transaction

from accounting.models import (
    AssetCategory,
    FixedAsset,
)


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

        return asset

    # =========================================================
    # ACTIVATE ASSET
    # =========================================================

    @staticmethod
    @transaction.atomic
    def activate_asset(
        *,
        asset,
        user,
    ):

        if asset.status != "draft":
            raise ValueError("Only draft asset can be activated")

        asset.status = "active"

        asset.updated_by = user

        asset.save()

        return asset
