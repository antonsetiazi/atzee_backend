# hrms/enums/attendance_status.py

from django.db import models


class AttendanceStatus(models.TextChoices):
    PRESENT = "present", "Present"
    LATE = "late", "Late"
    ABSENT = "absent", "Absent"
    LEAVE = "leave", "Leave"
    HOLIDAY = "holiday", "Holiday"
