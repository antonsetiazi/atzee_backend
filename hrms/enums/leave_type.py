# hrms/enums/leave_type.py

from django.db import models


class LeaveType(models.TextChoices):
    ANNUAL = "annual", "Annual Leave"
    SICK = "sick", "Sick Leave"
    MATERNITY = "maternity", "Maternity Leave"
    PATERNITY = "paternity", "Paternity Leave"
    UNPAID = "unpaid", "Unpaid Leave"
    SPECIAL = "special", "Special Leave"
