# accounting/services/asset_disposal_service.py

from decimal import Decimal

from django.db import transaction

from accounting.models import (
    Account,
    AssetDisposal,
    FixedAsset,
)
from accounting.services.journal_service import JournalService
from core.activity.constants.activity_types import FIXED_ASSET
from core.activity.events.finance_events import FinanceEvents
from core.activity.services.activity_service import ActivityService


class AssetDisposalService:

    @staticmethod
    @transaction.atomic
    def dispose_asset(
        *,
        tenant,
        user,
        asset_id,
        disposal_date,
        disposal_value,
        notes="",
    ):

        asset = FixedAsset.objects.select_related("category").get(
            id=asset_id,
            tenant=tenant,
            is_deleted=False,
        )

        if asset.status != "active":
            raise ValueError("Only active assets can be disposed")

        disposal_value = Decimal(str(disposal_value))
        category = asset.category

        # =====================================================
        # CALCULATE
        # =====================================================
        book_value = asset.book_value
        gain_loss = Decimal(str(disposal_value)) - Decimal(str(book_value))

        # =====================================================
        # GET ACCOUNTS
        # =====================================================
        asset_account = category.asset_account
        accumulated_account = category.accumulated_depreciation_account
        cash_account = Account.objects.get(
            tenant=tenant,
            code="1110",  # temporary
        )

        gain_account = Account.objects.get(
            tenant=tenant,
            code="4200",
        )

        loss_account = Account.objects.get(
            tenant=tenant,
            code="5400",
        )

        real_accumulated = Decimal(str(asset.purchase_cost)) - Decimal(
            str(asset.book_value)
        )

        # =====================================================
        # BUILD JOURNAL
        # =====================================================
        entries_data = [
            {
                "account_id": cash_account.id,
                "debit": disposal_value,
                "credit": 0,
                "description": ("Asset disposal proceeds"),
            },
            {
                "account_id": (accumulated_account.id),
                "debit": real_accumulated,
                "credit": 0,
                "description": ("Reverse accumulated depreciation"),
            },
            {
                "account_id": asset_account.id,
                "debit": 0,
                "credit": (asset.purchase_cost),
                "description": ("Remove fixed asset"),
            },
        ]

        # =====================================================
        # GAIN / LOSS
        # =====================================================
        if gain_loss > Decimal("0"):
            entries_data.append(
                {
                    "account_id": gain_account.id,
                    "debit": 0,
                    "credit": gain_loss,
                    "description": ("Gain on disposal"),
                }
            )

        elif gain_loss < Decimal("0"):
            entries_data.append(
                {
                    "account_id": loss_account.id,
                    "debit": abs(gain_loss),
                    "credit": 0,
                    "description": ("Loss on disposal"),
                }
            )

        total_debit = sum(Decimal(str(x["debit"])) for x in entries_data)
        total_credit = sum(Decimal(str(x["credit"])) for x in entries_data)

        if total_debit != total_credit:
            raise ValueError(
                f"Disposal journal not balanced. "
                f"Debit={total_debit} "
                f"Credit={total_credit}"
            )

        # =====================================================
        # CREATE JOURNAL
        # =====================================================
        journal = JournalService.create_journal(
            tenant=tenant,
            user=user,
            date=disposal_date,
            description=(f"Asset Disposal " f"{asset.asset_number}"),
            reference=(f"DISP-{asset.asset_number}"),
            entries_data=entries_data,
            auto_post=True,
        )

        # =====================================================
        # CREATE DISPOSAL RECORD
        # =====================================================
        disposal = AssetDisposal.objects.create(
            tenant=tenant,
            asset=asset,
            disposal_date=disposal_date,
            disposal_value=disposal_value,
            gain_loss_amount=gain_loss,
            notes=notes,
            journal=journal,
            status="posted",
            created_by=user,
        )

        # =====================================================
        # UPDATE ASSET
        # =====================================================
        asset.status = "disposed"
        asset.updated_by = user
        asset.save()

        # =====================================================
        # RECORD ACTIVITY
        # =====================================================
        ActivityService.record(
            tenant=tenant,
            target_type=FIXED_ASSET,
            target_id=asset.id,
            event=FinanceEvents.FIXED_ASSET_DISPOSED,
            title="Fixed asset disposed",
            description=(f"Asset '{asset.name}' has been disposed"),
            severity="warning",
            created_by=user,
            metadata={
                "asset_number": asset.asset_number,
                "disposal_value": str(disposal_value),
                "gain_loss_amount": str(gain_loss),
                "disposal_date": str(disposal_date),
            },
        )

        return disposal
