# core/activity/models/activity.py

from django.db import models

from core.models.base import TenantAwareModel
from core.users.models import User


class Activity(TenantAwareModel):
    """
    Universal tenant-aware activity event.

    Core operational event infrastructure used for:
    - audit trail
    - timeline
    - workflow visibility
    - notifications
    - realtime events
    - compliance logging
    """

    # =========================================================
    # TARGET REFERENCE (POLYMORPHIC)
    # =========================================================

    target_type = models.CharField(
        max_length=100,
        db_index=True,
        help_text="Entity type. Example: fixed_asset, invoice, employee",
    )

    target_id = models.UUIDField(db_index=True, help_text="Target entity UUID")

    # =========================================================
    # EVENT INFORMATION
    # =========================================================

    event = models.CharField(
        max_length=150,
        db_index=True,
        help_text="Namespaced event name. Example: finance.invoice.created",
    )

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    metadata = models.JSONField(
        default=dict,
        blank=True,
        help_text="Flexible structured event metadata",
    )

    # =========================================================
    # EVENT CLASSIFICATION
    # =========================================================

    visibility = models.CharField(
        max_length=20,
        default="internal",
        db_index=True,
        help_text="public/internal/private/system",
    )

    severity = models.CharField(
        max_length=20,
        default="info",
        db_index=True,
        help_text="info/success/warning/error/critical",
    )

    source = models.CharField(
        max_length=50,
        default="system",
        help_text="system/api/import/websocket/automation",
    )

    # =========================================================
    # OPTIONAL ACTOR OVERRIDE
    # =========================================================

    actor = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="activity_actor_set",
        help_text="Explicit event actor if different from created_by",
    )

    # =========================================================
    # SYSTEM FLAGS
    # =========================================================

    is_pinned = models.BooleanField(default=False)

    is_immutable = models.BooleanField(
        default=False,
        help_text="Prevent deletion/modification for compliance logs",
    )

    class Meta:
        db_table = "core_activities"
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["tenant", "target_type", "target_id"]),
            models.Index(fields=["tenant", "event"]),
            models.Index(fields=["tenant", "created_at"]),
            models.Index(fields=["tenant", "severity"]),
            models.Index(fields=["tenant", "visibility"]),
        ]

    def __str__(self):
        return f"{self.event} ({self.target_type})"
