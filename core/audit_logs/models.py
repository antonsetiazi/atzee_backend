from django.db import models
from core.tenants.models import Tenant
from core.users.models import User


class AuditLog(models.Model):
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name ="audit_logs"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    action = models.CharField(max_length=100)
    resource = models.CharField(max_length=100)
    resource_id = models.CharField(max_length=100, blank=True)

    metadata = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "core_audit_logs"


    def __str__(self):
        return f"{self.action} - {self.resource}"