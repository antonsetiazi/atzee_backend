# accounting/services/depreciation_service.py

from decimal import ROUND_HALF_UP, Decimal

from django.db import transaction

from accounting.models import DepreciationEntry
from accounting.services.journal_service import (
    JournalService,
)


class DepreciationService:
    # =========================================================
    # CALCULATE MONTHLY DEPRECIATION
    # =========================================================

    @staticmethod
    def calculate_monthly_depreciation(asset):
        depreciable_amount = asset.purchase_cost - asset.salvage_value
        monthly = depreciable_amount / Decimal(asset.useful_life_months)

        return monthly.quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        )

    # =========================================================
    # RUN SINGLE ASSET DEPRECIATION
    # =========================================================

    @staticmethod
    @transaction.atomic
    def run_asset_depreciation(
        *,
        asset,
        period_date,
        user,
    ):

        # =====================================================
        # VALIDATION
        # =====================================================
        if asset.status != "active":
            raise ValueError("Only active assets can be depreciated")

        if asset.book_value <= 0:
            raise ValueError("Asset already fully depreciated")

        existing = DepreciationEntry.objects.filter(
            tenant=asset.tenant,
            asset=asset,
            period_date=period_date,
            status__in=["draft", "posted"],
        ).exists()

        if existing:
            raise ValueError("Depreciation already exists for this period")

        # =====================================================
        # CALCULATE
        # =====================================================
        depreciation_amount = (
            DepreciationService.calculate_monthly_depreciation(asset)
        )

        remaining_book_value = asset.book_value - depreciation_amount

        # prevent negative
        if remaining_book_value < 0:
            depreciation_amount = asset.book_value
            remaining_book_value = Decimal("0")

        accumulated = asset.accumulated_depreciation + depreciation_amount

        # =====================================================
        # CREATE ENTRY
        # =====================================================
        entry = DepreciationEntry.objects.create(
            tenant=asset.tenant,
            asset=asset,
            period_date=period_date,
            depreciation_amount=(depreciation_amount),
            accumulated_depreciation=(accumulated),
            book_value_after=(remaining_book_value),
            status="draft",
            created_by=user,
        )

        # =====================================================
        # CREATE JOURNAL
        # =====================================================

        category = asset.category

        journal = JournalService.create_journal(
            tenant=asset.tenant,
            user=user,
            date=period_date,
            description=(f"Depreciation " f"{asset.asset_number}"),
            reference=(f"DEP-{asset.asset_number}"),
            entries_data=[
                {
                    "account_id": (category.depreciation_expense_account.id),
                    "debit": depreciation_amount,
                    "credit": 0,
                    "description": ("Depreciation Expense"),
                },
                {
                    "account_id": (
                        category.accumulated_depreciation_account.id
                    ),
                    "debit": 0,
                    "credit": depreciation_amount,
                    "description": ("Accumulated Depreciation"),
                },
            ],
            auto_post=True,
        )

        entry.journal = journal
        entry.status = "posted"
        entry.save()

        # =====================================================
        # UPDATE ASSET SNAPSHOT
        # =====================================================
        asset.accumulated_depreciation = accumulated
        asset.book_value = remaining_book_value
        asset.last_depreciation_date = period_date

        # fully depreciated
        if remaining_book_value <= 0:
            asset.status = "fully_depreciated"

        asset.updated_by = user
        asset.save()

        return entry
