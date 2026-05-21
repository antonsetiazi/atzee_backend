# hrms/enums/employment_type.py

from django.db import models


class EmploymentType(models.TextChoices):
    FULL_TIME = "full_time", "Full Time"
    PART_TIME = "part_time", "Part Time"
    CONTRACT = "contract", "Contract"
    FREELANCE = "freelance", "Freelance"
    INTERN = "intern", "Intern"
