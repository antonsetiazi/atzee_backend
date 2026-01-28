from rest_framework import serializers
from accounting.journals.models import Journal, JournalLine


class JournalLineSerializer(serializers.ModelSerializer):
    account_code = serializers.CharField(
        source="account.code",
        read_only=True
    )
    account_name = serializers.CharField(
        source="account.name",
        read_only=True
    )

    class Meta:
        model = JournalLine
        fields = [
            "id",
            "account_code",
            "account_name",
            "debit",
            "credit",
            "memo",
        ]


class JournalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = [
            "id",
            "journal_number",
            "journal_type",
            "journal_date",
            "description",
            "status",
        ]


class JournalDetailSerializer(serializers.ModelSerializer):
    lines = JournalLineSerializer(many=True, read_only=True)

    class Meta:
        model = Journal
        fields = [
            "id",
            "journal_number",
            "journal_type",
            "journal_date",
            "description",
            "source_app",
            "source_id",
            "status",
            "reversed_from",
            "lines",
            "created_at",
            "updated_at",
        ]