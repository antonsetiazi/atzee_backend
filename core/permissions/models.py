from django.db import models
from core.tenants.models import Tenant


class Permission(models.Model):
    """
    Permission atomic unit.
    Example:
        code = "inventory.item.create"
    """
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="permissions"
    )

    code = models.CharField(max_length=150)
    description = models.TextField(blank=True)


    class Meta:
        db_table = "core_permissions"
        unique_together = ("tenant", "code")


    def __str__(self):
        return self.code
    

class RolePermission(models.Model):
    role = models.ForeignKey(
        "core_roles.Role",
        on_delete=models.CASCADE,
        related_name="role_permissions"
    )
    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        related_name="permission_roles"
    )


    class Meta:
        db_table = "core_role_permissions"
        unique_together = ("role", "permission")