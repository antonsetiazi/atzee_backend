# core/activity/models/activity_comment.py

from django.db import models

from core.activity.models.activity import Activity
from core.models.base import TenantAwareModel


class ActivityComment(TenantAwareModel):
    """
    User discussion/comment attached to activity event.

    Enables:
    - internal discussion
    - approval notes
    - operational collaboration
    """

    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="comments"
    )

    content = models.TextField()

    is_internal = models.BooleanField(default=True)

    class Meta:
        db_table = "core_activity_comments"

        ordering = ["created_at"]

    def __str__(self):
        return f"Comment on {self.activity_id}"
