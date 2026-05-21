# hrms/models/employee.py

from django.db import models

from core.models.base import TenantAwareModel
from core.org.departments.models import Department
from core.users.models import User
from hrms.enums import (
    ContractType,
    EmployeeStatus,
    EmploymentType,
    Gender,
    PositionLevel,
)


class Position(TenantAwareModel):
    """
    Workforce position / job title.
    Example:
    - Backend Engineer
    - HR Manager
    - Accountant
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    level = models.CharField(
        max_length=30, choices=PositionLevel.choices, blank=True
    )

    class Meta:
        db_table = "hrms_positions"
        ordering = ["name"]
        unique_together = ("tenant", "code")

    def __str__(self):
        return self.name


class Employee(TenantAwareModel):
    """
    Workforce employee entity.
    Employee != User.
    """

    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="employee_profile",
    )

    employee_id = models.CharField(max_length=50)

    full_name = models.CharField(max_length=255)

    email = models.EmailField(blank=True)

    phone = models.CharField(max_length=50, blank=True)

    gender = models.CharField(
        max_length=20, choices=Gender.choices, blank=True
    )

    birth_date = models.DateField(null=True, blank=True)

    department = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="employees",
    )

    position = models.ForeignKey(
        Position,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="employees",
    )

    manager = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="subordinates",
    )

    join_date = models.DateField(null=True, blank=True)

    employment_status = models.CharField(
        max_length=30, choices=EmployeeStatus.choices, default="active"
    )

    contract_type = models.CharField(
        max_length=30,
        choices=ContractType.choices,
        default=ContractType.PERMANENT,
    )

    employment_type = models.CharField(
        max_length=30,
        choices=EmploymentType.choices,
        default=EmploymentType.FULL_TIME,
    )

    class Meta:
        db_table = "hrms_employees"
        ordering = ["full_name"]
        unique_together = ("tenant", "employee_id")

    def __str__(self):
        return f"{self.employee_id} - {self.full_name}"
