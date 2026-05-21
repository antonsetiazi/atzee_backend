# hrms/models/leave.py

from django.db import models

from core.models.base import TenantAwareModel
from hrms.enums import (
    LeaveStatus,
    LeaveType,
)
from hrms.models.employee import Employee


class LeaveRequest(TenantAwareModel):
    """
    Employee leave request.
    """

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="leave_requests"
    )

    leave_type = models.CharField(max_length=30, choices=LeaveType.choices)

    start_date = models.DateField()

    end_date = models.DateField()

    reason = models.TextField(blank=True)

    status = models.CharField(
        max_length=30, choices=LeaveStatus.choices, default=LeaveStatus.PENDING
    )

    approved_by = models.ForeignKey(
        Employee,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="approved_leave_requests",
    )

    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "hrms_leave_requests"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"
