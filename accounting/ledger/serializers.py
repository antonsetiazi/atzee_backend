# accounting/ledger/serializers.py

from rest_framework import serializers
from accounting.ledger.models import LedgerEntry


class LedgerEntrySerializer(serializers.ModelSerializer):
    account_code = serializers.CharField(read_only=True)
    account_name = serializers.CharField(read_only=True)

    class Meta:
        model = LedgerEntry
        fields = [
            "id",
            "entry_date",
            "account",
            "account_code",
            "account_name",
            "debit",
            "credit",
            "balance_direction",
            "journal",
        ]
        read_only_fields = fields
