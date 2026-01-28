from django.db import models
from shared.models import TenantAwareModel


class AttendanceRecord(TenantAwareModel):
    """
    Daily attendance record for an employee.
    Immutable per employee per date.
    """

    STATUS_PRESENT = "present"
    STATUS_ABSENT = "absent"
    STATUS_LEAVE = "leave"
    STATUS_SICK = "sick"
    STATUS_OFF = "off"

    STATUS_CHOICES = [
        (STATUS_PRESENT, "Present"),
        (STATUS_ABSENT, "Absent"),
        (STATUS_LEAVE, "Leave"),
        (STATUS_SICK, "Sick"),
        (STATUS_OFF, "Off Day"),
    ]

    employee_id = models.PositiveIntegerField(
        help_text="FK to hr.employees.Employee.id"
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PRESENT
    )

    check_in = models.DateTimeField(
        blank=True,
        null=True
    )

    check_out = models.DateTimeField(
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = "hr_attendance_records"
        unique_together = (
            ("tenant", "employee_id", "date"),
        )
        ordering = ["-date"]

    def __str__(self):
        return f"{self.employee_id} - {self.date}"
