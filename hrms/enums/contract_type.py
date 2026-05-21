# hrms/enums/contract_type.py

from django.db import models


class ContractType(models.TextChoices):
    PERMANENT = "permanent", "Permanent"
    CONTRACT = "contract", "Contract"
    FREELANCE = "freelance", "Freelance"
    INTERN = "intern", "Intern"
    PART_TIME = "part_time", "Part Time"
