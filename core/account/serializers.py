# core/account/serializers.py

from rest_framework import serializers
from core.account.models import UserSettings


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = [
            "theme",
            "language",
            "timezone",
            "email_notifications",
        ]
