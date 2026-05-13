# core/activity/api/filters.py

import django_filters

from core.activity.models import Activity


class ActivityFilter(django_filters.FilterSet):
    """
    Enterprise-grade activity filtering.
    """

    target_type = django_filters.CharFilter(field_name="target_type")

    target_id = django_filters.UUIDFilter(field_name="target_id")

    event = django_filters.CharFilter(field_name="event")

    severity = django_filters.CharFilter(field_name="severity")

    visibility = django_filters.CharFilter(field_name="visibility")

    created_by = django_filters.UUIDFilter(field_name="created_by")

    created_at_after = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )

    created_at_before = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )

    class Meta:
        model = Activity

        fields = [
            "target_type",
            "target_id",
            "event",
            "severity",
            "visibility",
            "created_by",
        ]
