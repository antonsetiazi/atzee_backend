# accounting/api/serializers/journal_serializer.py

from rest_framework import serializers
from accounting.models import Journal, JournalEntry


class JournalEntrySerializer(serializers.ModelSerializer):
    account_code = serializers.CharField(source="account.code", read_only=True)
    account_name = serializers.CharField(source="account.name", read_only=True)

    class Meta:
        model = JournalEntry
        fields = [
            "id",
            "account",
            "account_code",
            "account_name",
            "debit",
            "credit",
            "description",
        ]


class JournalSerializer(serializers.ModelSerializer):
    entries = JournalEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Journal
        fields = [
            "id",
            "date",
            "description",
            "reference",
            "source",
            "is_posted",
            "posted_at",
            "entries",
        ]