# business/partners/models/service_profile.py

from django.db import models
from business.partners.models import Partner


class PartnerServiceProfile(models.Model):
    """
    Extension khusus untuk partner bertipe service (ustadz, tutor, dll)
    """

    partner = models.OneToOneField(
        Partner,
        on_delete=models.CASCADE,
        related_name="service_profile",
    )

    specialization = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    experience_years = models.PositiveIntegerField(
        default=0
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "business_partners_service_profile"

    def __str__(self):
        return f"ServiceProfile({self.partner.name})"