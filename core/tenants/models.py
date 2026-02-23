# core/tenants/models.py

from django.db import models
from django.conf import settings
import uuid


class Tenant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    branding = models.JSONField(default=dict, blank=True)
    
    platform_fee_percent = models.DecimalField(
        max_digits=5, decimal_places=2, default=0
    )
    
    VERTICAL_CHOICES = (
        ("core", "Core Platform"),
        ("ustadzku", "Ustadzku"),
        ("clinic", "Clinic"),
        ("school", "School"),
    )
    
    vertical = models.CharField(
        max_length=50,
        choices=VERTICAL_CHOICES,
        default="core",
        db_index=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "core_tenants"

    def __str__(self):
        return self.name
    

class UserTenant(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tenant_memberships"
    )
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="user_memberships"
    )

    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "core_user_tenants"
        unique_together = ("user", "tenant")