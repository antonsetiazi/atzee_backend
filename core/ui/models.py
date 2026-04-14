# core/ui/models.py

from django.db import models
from core.tenants.models import Tenant

class UIMenu(models.Model):
    """
    Menu node definition (agnostic to frontend framework)
    """
    key = models.CharField(max_length=100, unique=True)
    label = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, null=True)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )

    app = models.CharField(max_length=100)
    resource = models.CharField(max_length=100)
    action = models.CharField(max_length=50)

    route = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.label


class UIPage(models.Model):
    """
    Declarative UI Page Schema
    Backend-driven UI contract
    """

    key = models.CharField(max_length=150, unique=True)
    title = models.CharField(max_length=150)
    subtitle = models.TextField(
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    
    domain = models.CharField(max_length=100)
    
    # frontend + api agree on this
    entity = models.CharField(max_length=100)

    path = models.CharField(max_length=200, blank=True, null=True)

    # permission gate (evaluated by service)
    permissions = models.JSONField(default=list)

    # ordered UI blocks (table, form, workflow, chart, etc)
    blocks = models.JSONField(default=list)
    
    data_source = models.CharField(max_length=200, blank=True, null=True)

    method = models.CharField(max_length=20, blank=True, null=True)
    
    accept_context = models.BooleanField(default=True)

    payload_from_context = models.JSONField(default=list, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    meta = models.JSONField(default=dict, blank=True)
    
    class Meta:
        ordering = ["key"]

    def __str__(self):
        return self.key


class TenantNavigationConfig(models.Model):
    """
    Tenant-specific navigation layout.
    type: sidebar, bottom, drawer
    """
    NAV_TYPE_CHOICES = [
        ("sidebar", "Sidebar"),
        ("bottom", "Bottom Navigation"),
        ("drawer", "Drawer"),
    ]

    DEVICE_CHOICES = [
        ("mobile", "Mobile"),
        ("desktop", "Desktop"),
        ("all", "All Devices"),
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="navigation_configs",
    )

    type = models.CharField(
        max_length=20,
        choices=NAV_TYPE_CHOICES,
    )

    device = models.CharField(
        max_length=20,
        choices=DEVICE_CHOICES,
        default="all",
    )

    app = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    role = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    is_default = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("tenant", "type", "device", "app", "role")

    def __str__(self):
        return f"{self.tenant.code} - {self.type}"


class TenantNavigationItem(models.Model):
    """
    Navigation item that can represent:
    - menu
    - page
    - entity
    - workflow
    - custom action
    """

    ACTION_TYPE_CHOICES = [
        ("menu", "Menu"),
        ("page", "Page"),
        ("entity", "Entity"),
        ("workflow", "Workflow"),
        ("custom", "Custom Route"),
    ]

    navigation = models.ForeignKey(
        TenantNavigationConfig,
        on_delete=models.CASCADE,
        related_name="items",
    )

    # Optional link to UIMenu (backward compatible)
    menu = models.ForeignKey(
        "UIMenu",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    action_type = models.CharField(
        max_length=20,
        choices=ACTION_TYPE_CHOICES,
    )

    # Flexible target
    target = models.CharField(
        max_length=150,
        help_text="Page key, entity key, workflow key, or route",
    )

    label_override = models.CharField(max_length=100, blank=True, null=True)
    icon_override = models.CharField(max_length=50, blank=True, null=True)

    route_override = models.CharField(max_length=200, blank=True, null=True)

    is_primary = models.BooleanField(default=False)

    badge_source = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        help_text="Entity key or service key for badge counter",
    )

    order = models.PositiveIntegerField(default=0)
    
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.navigation} → {self.menu.label}"