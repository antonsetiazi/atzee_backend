# accounting/api/taxes/serializers.py

from rest_framework import serializers

from accounting.models import Tax


class TaxSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Tax

        fields = "__all__"

        read_only_fields = [
            "id",
            "tenant",
            "created_at",
            "updated_at",
        ]