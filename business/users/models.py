# business/users/models.py

from django.db import models
from core.models.base import TenantAwareModel, ExtensibleModel
from core.users.models import User


class BusinessUser(TenantAwareModel, ExtensibleModel):
    """
    Domain user (pemesan layanan ustadz).
    Linked to core user for authentication.
    """

    core_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="business_profile"
    )

    name = models.CharField(max_length=255)

    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    organization_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Masjid / lembaga / komunitas"
    )

    organization_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Masjid / Individu / Komunitas / dll"
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = "business_users"
        ordering = ["name"]

    def __str__(self):
        return self.name
