# core/roles/models.py

from django.db import models
from core.tenants.models import Tenant


class Role(models.Model):
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="roles"
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    # ENGINE FIELD
    access_level = models.PositiveIntegerField(
        help_text="Semakin besar, semakin tinggi akses"
    )

    users = models.ManyToManyField(
        "core_users.User",
        through="core_roles.UserRole",
        related_name="roles"
    )

    is_system = models.BooleanField(default=True)

    class Meta:
        db_table = "core_roles"
        unique_together = ("tenant", "name")
        ordering = ["access_level"]

    
    def __str__(self):
        return f"{self.name} ({self.access_level})"
    

class UserRole(models.Model):
    user = models.ForeignKey(
        "core_users.User",
        on_delete=models.CASCADE,
        related_name="user_roles"
    )
    role = models.ForeignKey(
        "core_roles.Role",
        on_delete=models.CASCADE,
        related_name="role_users"
    )

    assigned_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = "core_user_roles"
        unique_together = ("user", "role")

    
    def __str__(self):
        return f"{self.user} → {self.role}"