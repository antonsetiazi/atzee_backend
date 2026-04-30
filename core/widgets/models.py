# core/widgets/models.py

from django.db import models
from core.models.base import TenantAwareModel, ExtensibleModel


class UIWidget(TenantAwareModel, ExtensibleModel):
    """
    Core Widget Engine model.
    Dynamic UI block rendered by frontend.
    """

    TYPE_CHOICES = [
        ("banner", "Banner"),
        ("video", "Video"),
        ("calendar", "Calendar"),
        ("market", "Market"),
        ("weather", "Weather"),
        ("kpi", "KPI"),
        ("reminder", "Reminder"),
    ]

    POSITION_CHOICES = [
        ("dashboard.main", "Dashboard Main"),
        ("dashboard.sidebar", "Dashboard Sidebar"),
        ("app.main", "App Main"),
        ("app.sidebar", "App Sidebar"),
    ]

    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES
    )

    position = models.CharField(
        max_length=100,
        choices=POSITION_CHOICES
    )

    title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    config = models.JSONField(
        default=dict,
        blank=True,
        help_text="Widget configuration payload"
    )

    starts_at = models.DateTimeField(
        blank=True,
        null=True
    )

    ends_at = models.DateTimeField(
        blank=True,
        null=True
    )

    target_roles = models.JSONField(
        default=list,
        blank=True
    )

    target_permissions = models.JSONField(
        default=list,
        blank=True
    )

    order = models.IntegerField(default=50)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_widgets"
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"{self.type} - {self.position}"
