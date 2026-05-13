# core/activity/api/views.py

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from core.activity.api.filters import ActivityFilter
from core.activity.api.serializers import ActivitySerializer
from core.activity.models import Activity
from core.tenants.services import TenantService


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Universal activity timeline endpoint.

    Supports:
    - audit trail
    - timeline feed
    - workflow history
    - realtime event stream source
    """

    serializer_class = ActivitySerializer

    permission_classes = [
        IsAuthenticated,
    ]

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]

    filterset_class = ActivityFilter

    ordering_fields = [
        "created_at",
    ]

    ordering = ["-created_at"]

    search_fields = [
        "title",
        "description",
        "event",
    ]

    def get_queryset(self):
        """
        Strict tenant isolation.
        """

        tenant = TenantService.get_current_tenant(self.request)

        if not tenant:
            return Activity.objects.none()

        queryset = (
            Activity.objects.filter(tenant=tenant)
            .select_related("created_by", "actor")
            .prefetch_related("attachments", "comments", "reactions")
        )

        return queryset
