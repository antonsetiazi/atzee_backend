# core/ui/models.py

from django.db import models


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
    description = models.TextField(
        blank=True,
        null=True
    )
    
    domain = models.CharField(max_length=100)
    
    # frontend + api agree on this
    entity = models.CharField(max_length=100)

    # permission gate (evaluated by service)
    permissions = models.JSONField(default=list)

    # ordered UI blocks (table, form, workflow, chart, etc)
    blocks = models.JSONField(default=list)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["key"]

    def __str__(self):
        return self.key
