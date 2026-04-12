# business/partners/models.py

from django.db import models
from django.conf import settings
from core.models.base import TenantAwareModel, ExtensibleModel
from django.core.validators import MinValueValidator, MaxValueValidator
from core.geo.countries.models import Country
from core.geo.regions.models import Region
from core.geo.cities.models import City
from core.geo.districts.models import District
from core.geo.villages.models import Village

class Partner(TenantAwareModel, ExtensibleModel):
    """
    Core partner model (business invariant).
    """

    core_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="partner_profile",
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Unique partner code per tenant"
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

    address = models.TextField(
        blank=True,
        null=True
    )

    country = models.ForeignKey(
        Country,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="partners"
    )

    region = models.ForeignKey(
        Region,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="partners"
    )

    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="partners"
    )

    district = models.ForeignKey(
        District,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="partners"
    )

    village = models.ForeignKey(
        Village,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="partners"
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    search_latitude = models.FloatField(null=True, db_index=True)
    search_longitude = models.FloatField(null=True, db_index=True)

    base_price = models.DecimalField(
        max_digits=14, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        db_index=True
    )
    
    rating_avg = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    rating_count = models.PositiveIntegerField(default=0)

    meta = models.JSONField(default=dict, blank=True)


    class Meta:
        db_table = "business_partners"
        unique_together = ("tenant", "code")
        ordering = ["name"]


    @property
    def location_label(self):
        if self.city:
            return self.city.name
        if self.region:
            return self.region.name
        return "Lokasi belum diatur"
    
    @property
    def city_name(self):
        return self.city.name if self.city else None

    def __str__(self):
        return self.name