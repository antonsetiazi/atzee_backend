# core/activity/models/activity_attachment.py

from django.db import models

from core.activity.models.activity import Activity
from core.models.base import TenantAwareModel


class ActivityAttachment(TenantAwareModel):
    """
    Attachment linked to activity events.

    Used for:
    - screenshots
    - invoices
    - approval documents
    - exported reports
    - evidence files
    """

    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="attachments"
    )

    file = models.FileField(upload_to="activity/attachments/%Y/%m/")

    file_name = models.CharField(max_length=255)

    file_size = models.BigIntegerField(default=0)

    mime_type = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "core_activity_attachments"

        ordering = ["created_at"]

    def __str__(self):
        return self.file_name
