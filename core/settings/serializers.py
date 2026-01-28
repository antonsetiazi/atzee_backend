from rest_framework import serializers
from core.settings.models import Setting


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = [
            "id",
            "key",
            "value",
            "tenant",
        ]
        read_only_fields = ["tenant"]
