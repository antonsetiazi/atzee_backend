# core/schedule/events/serializers.py

from rest_framework import serializers
from core.schedule.events.models import Event


class EventListSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.full_name", read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "start_datetime",
            "end_datetime",
            "all_day",
            "created_by",
        ]


class EventDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.full_name", read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "start_datetime",
            "end_datetime",
            "all_day",
            "participants",
            "color",
            "metadata",
            "created_at",
            "updated_at",
            "created_by",
        ]


class EventCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField()
    all_day = serializers.BooleanField(required=False)
    participants = serializers.JSONField(required=False)
    color = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.JSONField(required=False)

    def validate(self, attrs):
        start = attrs.get("start_datetime")
        end = attrs.get("end_datetime")

        if start >= end:
            raise serializers.ValidationError(
                "start_datetime must be before end_datetime."
            )
        return attrs


class EventUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False, allow_blank=True)
    start_datetime = serializers.DateTimeField(required=False)
    end_datetime = serializers.DateTimeField(required=False)
    all_day = serializers.BooleanField(required=False)
    participants = serializers.JSONField(required=False)
    color = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.JSONField(required=False)

    def validate(self, attrs):
        instance: Event = self.instance

        start = attrs.get("start_datetime", instance.start_datetime)
        end = attrs.get("end_datetime", instance.end_datetime)

        if start >= end:
            raise serializers.ValidationError(
                "start_datetime must be before end_datetime."
            )
        return attrs
