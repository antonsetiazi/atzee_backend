# core/fees/api/serializers.py

from rest_framework import serializers
from core.fees.models import FeeConfig


class FeeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeConfig
        fields = "__all__"