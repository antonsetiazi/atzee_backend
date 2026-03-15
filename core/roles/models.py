# core/roles/models.py

from django.db import models
from core.tenants.models import Tenant
from core.roles.enums import RoleCode


class Role(models.Model):
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="roles"
    )

    code = models.CharField(
        max_length=50,
        choices=[(r.value, r.value) for r in RoleCode],
        db_index=True,
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

    is_default = models.BooleanField(
        default=False,
        help_text="Default role for new users in this tenant"
    )

    class Meta:
        db_table = "core_roles"
        unique_together = ("tenant", "code")
        ordering = ["access_level"]

    
    def __str__(self):
        return f"{self.name} ({self.code})"
    

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