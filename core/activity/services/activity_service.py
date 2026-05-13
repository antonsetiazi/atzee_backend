# core/activity/services/activity_service.py

from typing import Optional
from uuid import UUID

from django.db import transaction

from core.activity.models import Activity
from core.activity.services.event_dispatcher import EventDispatcher
from core.tenants.models import Tenant
from core.users.models import User


class ActivityService:
    """
    Universal activity recorder service.

    This is the SINGLE ENTRY POINT for creating activities.

    DO NOT create Activity directly from:
    - views
    - serializers
    - business modules

    Always use this service.
    """

    @staticmethod
    @transaction.atomic
    def record(
        *,
        tenant: Tenant,
        target_type: str,
        target_id: UUID,
        event: str,
        title: str,
        description: str = "",
        metadata: Optional[dict] = None,
        created_by: Optional[User] = None,
        actor: Optional[User] = None,
        visibility: str = "internal",
        severity: str = "info",
        source: str = "system",
        is_pinned: bool = False,
        is_immutable: bool = False,
    ) -> Activity:
        """
        Create and dispatch a universal activity event.
        """

        activity = Activity.objects.create(
            tenant=tenant,
            target_type=target_type,
            target_id=target_id,
            event=event,
            title=title,
            description=description,
            metadata=metadata or {},
            created_by=created_by,
            actor=actor,
            visibility=visibility,
            severity=severity,
            source=source,
            is_pinned=is_pinned,
            is_immutable=is_immutable,
        )

        # =====================================================
        # DISPATCH PIPELINE
        # =====================================================

        EventDispatcher.dispatch(activity)

        return activity
