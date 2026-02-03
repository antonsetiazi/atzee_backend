# accounting/chart_of_accounts/entities/chart_of_account_create.py

from core.entities.contracts import BaseEntity
from accounting.chart_of_accounts.models import ChartOfAccount, AccountType
from django.core.exceptions import ValidationError


class ChartOfAccountCreateEntity(BaseEntity):
    """
    chart_of_accounts.create entity

    Creates a new Chart of Account.
    """

    key = "chart_of_accounts.create"          # ✅ ENTITY PURE
    domain = "accounting"
    permission = "accounting.chart_of_accounts.add"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        query format (from frontend):
        {
            code: str,
            name: str,
            account_type: "ASSET" | "LIABILITY" | "EQUITY" | "INCOME" | "EXPENSE",
            parent_id?: str,
            is_postable?: bool
        }
        """

        # ----------------------------
        # Required fields
        # ----------------------------
        code = (query.get("code") or "").strip()
        name = (query.get("name") or "").strip()
        account_type = query.get("account_type")

        if not code:
            raise ValidationError("Account code is required")

        if not name:
            raise ValidationError("Account name is required")

        if account_type not in AccountType.values:
            raise ValidationError("Invalid account type")

        # ----------------------------
        # Uniqueness (tenant invariant)
        # ----------------------------
        if ChartOfAccount.objects.filter(
            tenant=tenant,
            code=code,
        ).exists():
            raise ValidationError("Account code already exists")

        # ----------------------------
        # Parent (optional)
        # ----------------------------
        parent = None
        parent_id = query.get("parent_id")

        if parent_id:
            try:
                parent = ChartOfAccount.objects.get(
                    id=parent_id,
                    tenant=tenant,
                )
            except ChartOfAccount.DoesNotExist:
                raise ValidationError("Parent account not found")

            # 🔒 Accounting invariant:
            # Parent must NOT be postable
            if parent.is_postable:
                raise ValidationError(
                    "Parent account must be non-postable"
                )

            # 🔒 Accounting invariant:
            # Parent account type must match
            if parent.account_type != account_type:
                raise ValidationError(
                    "Parent account type must match child account type"
                )

        # ----------------------------
        # Flags
        # ----------------------------
        is_postable = bool(query.get("is_postable", True))

        # ----------------------------
        # Create
        # ----------------------------
        account = ChartOfAccount.objects.create(
            tenant=tenant,
            code=code,
            name=name,
            account_type=account_type,
            parent=parent,
            is_postable=is_postable,
            created_by=user,
        )

        return {
            "id": str(account.id),
            "message": "Chart of Account created successfully",
        }
