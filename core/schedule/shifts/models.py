# core/schedule/models/shift.py

from django.db import models
from django.core.exceptions import ValidationError

from core.models.base import TenantAwareModel, ExtensibleModel


class Shift(TenantAwareModel, ExtensibleModel):
    """
    Generic schedule shift engine.

    - Does NOT know HR, payroll, attendance, etc.
    - Pure scheduling + participant assignment.
    """

    name = models.CharField(max_length=100)

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    metadata = models.JSONField(
        blank=True,
        null=True,
        help_text="Custom metadata for vertical/business modules",
    )

    participants = models.ManyToManyField(
        "core_users.User",
        through="ShiftParticipant",
        through_fields=("shift", "user"),
        related_name="shifts",
        blank=True,
    )

    class Meta:
        db_table = "core_schedule_shifts"
        ordering = ["start_datetime"]

    def clean(self):
        if self.end_datetime <= self.start_datetime:
            raise ValidationError(
                {"end_datetime": "end_datetime must be greater than start_datetime."}
            )

    def __str__(self):
        return self.name


class ShiftParticipant(TenantAwareModel):
    """
    Through model to assign users into shifts.
    Keeps relational integrity & tenant safety.
    """

    shift = models.ForeignKey(
        Shift,
        on_delete=models.CASCADE,
        related_name="shift_participants",
    )

    user = models.ForeignKey(
        "core_users.User",
        on_delete=models.CASCADE,
        related_name="user_shift_participations",
    )

    role = models.CharField(
        max_length=50,
        blank=True,
        help_text="Optional role inside shift (leader, backup, etc)",
    )

    class Meta:
        db_table = "core_schedule_shift_participants"
        unique_together = ("shift", "user")

    def __str__(self):
        return f"{self.shift.name} - {self.user}"

