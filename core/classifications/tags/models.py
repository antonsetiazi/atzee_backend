# core/classifications/tags/models.py

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from core.models.base import TenantAwareModel


class Tag(TenantAwareModel):
    """
    Flat classification tag.
    Example: urgent, vip, internal
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")

    class Meta:
        db_table = "core_tags"
        unique_together = ("tenant", "code")
        indexes = [
            models.Index(fields=["tenant", "code"]),
            models.Index(fields=["tenant", "name"]),
        ]

    def __str__(self):
        return self.name


class TagRelation(TenantAwareModel):
    """
    Generic tag relation engine.
    """

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="relations",
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )

    object_id = models.PositiveBigIntegerField()

    content_object = GenericForeignKey(
        "content_type",
        "object_id",
    )

    class Meta:
        db_table = "core_tag_relations"

        unique_together = (
            "tenant",
            "tag",
            "content_type",
            "object_id",
        )

        indexes = [
            models.Index(fields=["tenant", "content_type", "object_id"]),
            models.Index(fields=["tenant", "tag"]),
            models.Index(fields=["tenant", "content_type", "tag"]),
        ]

    def clean(self):
        if self.tag.tenant_id != self.tenant_id:
            raise ValidationError("Tag tenant mismatch.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
