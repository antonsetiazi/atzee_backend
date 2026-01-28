from django.db import models
from core.tenants.models import Tenant


class Setting(models.Model):
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="settings"
    )

    key = models.CharField(max_length=100)
    value = models.JSONField


    class Meta:
        db_table = "core_settings"
        unique_together = ("tenant", "key")


    def __str__(self):
        return f"{self.key} ({self.tenant_id or 'GLOBAL'})"