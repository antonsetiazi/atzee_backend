# core/legal/models.py

from django.db import models
from django.db.models import Q
from core.models.base import TenantAwareModel
from django.conf import settings


class PolicyDocument(TenantAwareModel):
    """
    Legal policy document (Terms, Privacy, etc).
    Versioned and tenant-aware.
    """

    POLICY_TYPES = (
        ("tos", "Terms of Service"),
        ("privacy", "Privacy Policy"),
        ("terms", "Terms & Conditions"),
    )

    code = models.CharField(max_length=50)
    title = models.CharField(max_length=255)

    policy_type = models.CharField(max_length=50, choices=POLICY_TYPES)
    content = models.TextField()

    version = models.IntegerField(default=1)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_policy_documents"
        constraints = [
            models.UniqueConstraint(
                fields=["tenant", "code", "version"],
                condition=Q(is_deleted=False),
                name="unique_active_policy_version",
            )
        ]
        ordering = ["policy_type", "-version"]

    def __str__(self):
        return f"[{self.policy_type}] v{self.version} - {self.title}"


class PolicyAcceptance(TenantAwareModel):
    """
    Track user acceptance of a policy version.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="policy_acceptances",
    )

    policy = models.ForeignKey(
        PolicyDocument,
        on_delete=models.CASCADE,
        related_name="acceptances",
    )

    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        db_table = "core_policy_acceptances"
        unique_together = (
            ("user", "policy"),
        )

    def __str__(self):
        return f"{self.user} accepted {self.policy}"