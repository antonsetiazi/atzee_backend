# hrms/enums/employee_status.py

from django.db import models


class EmployeeStatus(models.TextChoices):
    PROBATION = "probation", "Probation"
    ACTIVE = "active", "Active"
    LEAVE = "leave", "Leave"
    SUSPENDED = "suspended", "Suspended"
    RESIGNED = "resigned", "Resigned"
    TERMINATED = "terminated", "Terminated"
    RETIRED = "retired", "Retired"
