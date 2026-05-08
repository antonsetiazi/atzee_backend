# accounting/api/cash_transactions/serializers.py

from rest_framework import serializers

from accounting.models import (
    CashTransaction
)


class CashTransactionSerializer(
    serializers.ModelSerializer
):

    from_account_name = serializers.CharField(
        source="from_account.name",
        read_only=True
    )

    to_account_name = serializers.CharField(
        source="to_account.name",
        read_only=True
    )

    class Meta:
        model = CashTransaction

        fields = [
            "id",

            "transaction_number",

            "transaction_type",

            "transaction_date",

            "from_account",
            "from_account_name",

            "to_account",
            "to_account_name",

            "amount",

            "reference",
            "description",
        ]