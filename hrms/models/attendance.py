# hrms/models/attendance.py

from django.db import models

from core.models.base import TenantAwareModel
from hrms.enums import AttendanceStatus
from hrms.models.employee import Employee


class Attendance(TenantAwareModel):
    """
    Employee attendance record.
    """

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="attendances"
    )

    attendance_date = models.DateField()

    check_in = models.DateTimeField(null=True, blank=True)

    check_out = models.DateTimeField(null=True, blank=True)

    status = models.CharField(
        max_length=30,
        choices=AttendanceStatus.choices,
        default=AttendanceStatus.PRESENT,
    )

    notes = models.TextField(blank=True)

    class Meta:
        db_table = "hrms_attendances"
        ordering = ["-attendance_date"]
        unique_together = ("tenant", "employee", "attendance_date")

    def __str__(self):
        return f"{self.employee} - {self.attendance_date}"
