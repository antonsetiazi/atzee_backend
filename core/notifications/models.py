from django.db import models
from core.users.models import User
from core.tenants.models import Tenant


class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notifications"
    )

    type = models.CharField(
        max_length=50,
        help_text="system | info | warning | error"
    )

    title = models.CharField(max_length=255)
    message = models.TextField()

    payload = models.JSONField(
        null=True,
        blank=True,
        help_text="Optional structured data for frontend navigation"
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "core_notifications"
        ordering = ["-created_at"]

    
    def __str__(self):
        return f"[{self.type}] {self.title}"