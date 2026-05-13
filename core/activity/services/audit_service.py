# core/activity/services/audit_service.py

from typing import Optional

from core.activity.services.activity_service import ActivityService
from core.activity.services.event_builder import EventBuilder
from core.users.models import User


class AuditService:
    """
    Enterprise-grade audit helper service.

    Focus:
    - change tracking
    - immutable logs
    - compliance history
    - before/after snapshots
    """

    @staticmethod
    def log_update(
        *,
        tenant,
        target_type,
        target_id,
        before: dict,
        after: dict,
        event: str,
        title: str,
        description: str = "",
        created_by: Optional[User] = None,
    ):
        """
        Create immutable audit log with diff tracking.
        """

        changes = EventBuilder.build_changes(
            before=before,
            after=after,
        )

        metadata = EventBuilder.build_metadata(changes=changes)

        return ActivityService.record(
            tenant=tenant,
            target_type=target_type,
            target_id=target_id,
            event=event,
            title=title,
            description=description,
            metadata=metadata,
            created_by=created_by,
            severity="info",
            visibility="internal",
            source="audit",
            is_immutable=True,
        )
