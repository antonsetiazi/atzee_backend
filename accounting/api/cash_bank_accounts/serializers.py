# accounting/api/cash_bank_accounts/serializers.py

from rest_framework import serializers

from accounting.models import (
    CashBankAccount
)


class CashBankAccountSerializer(
    serializers.ModelSerializer
):

    accounting_account_code = (
        serializers.CharField(
            source="accounting_account.code",
            read_only=True
        )
    )

    accounting_account_name = (
        serializers.CharField(
            source="accounting_account.name",
            read_only=True
        )
    )

    class Meta:
        model = CashBankAccount

        fields = [
            "id",

            "name",
            "code",

            "account_type",

            "bank_name",
            "bank_account_number",
            "account_holder_name",

            "accounting_account",
            "accounting_account_code",
            "accounting_account_name",

            "current_balance",

            "is_default",
        ]