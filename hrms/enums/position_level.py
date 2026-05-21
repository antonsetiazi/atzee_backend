# hrms/enums/position_level.py

from django.db import models


class PositionLevel(models.TextChoices):
    STAFF = "staff", "Staff"
    SENIOR = "senior", "Senior"
    LEAD = "lead", "Lead"
    SUPERVISOR = "supervisor", "Supervisor"
    MANAGER = "manager", "Manager"
    DIRECTOR = "director", "Director"
    EXECUTIVE = "executive", "Executive"
