# backend/core/activity/models/activity_reaction.py

from django.db import models

from core.activity.models.activity import Activity
from core.models.base import TenantAwareModel
from core.users.models import User


class ActivityReaction(TenantAwareModel):
    """
    Lightweight reactions for collaboration UX.

    Examples:
    - like
    - approve
    - acknowledge
    - warning
    """

    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="reactions"
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="activity_reactions"
    )

    reaction = models.CharField(max_length=50)

    class Meta:
        db_table = "core_activity_reactions"

        unique_together = (("activity", "user", "reaction"),)

        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user} -> {self.reaction}"
