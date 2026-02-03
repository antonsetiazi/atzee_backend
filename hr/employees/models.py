# hr/employees/models.py

from django.db import models
from shared.models import TenantAwareModel


class Employee(TenantAwareModel):
    """
    Employee aggregate root (HR domain).
    Represents employment identity, not auth identity.
    """

    user_id = models.UUIDField(
        blank=True,
        null=True,
        help_text="Reference to core.users.User.id"
    )

    employee_code = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    full_name = models.CharField(
        max_length=255
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    job_title = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    join_date = models.DateField()

    notes = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = "hr_employees"
        unique_together = (
            ("tenant", "employee_code"),
            ("tenant", "user_id"),
        )
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name
    