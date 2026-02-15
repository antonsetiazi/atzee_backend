# core/geo/spatial/models.py

from django.db import models
from core.models.base import TenantAwareModel


class GeoLocation(TenantAwareModel):
    """
    Spatial location attached to any entity.

    This model represents a geographic coordinate
    (latitude & longitude) bound to an entity
    via related_entity + related_id.

    Domain-agnostic.
    """

    related_entity = models.CharField(
        max_length=100,
        help_text="Target entity key (e.g. customers, assets)"
    )

    related_id = models.CharField(
        max_length=64,
        help_text="Target entity ID"
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Latitude in WGS84 format"
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Longitude in WGS84 format"
    )

    label = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional location label"
    )

    metadata = models.JSONField(
        default=dict,
        blank=True,
        help_text="Optional spatial metadata"
    )

    class Meta:
        db_table = "core_geo_locations"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["tenant", "related_entity", "related_id"]),
        ]

    def __str__(self):
        return f"{self.related_entity}:{self.related_id} ({self.latitude},{self.longitude})"
