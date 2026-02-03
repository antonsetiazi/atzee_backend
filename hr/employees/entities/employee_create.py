# hr/employees/entities/employees_create.py

from core.entities.contracts import BaseEntity
from hr.employees.models import Employee
from core.users.models import User
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class EmployeesCreateEntity(BaseEntity):
    """
    employees.create entity

    Creates a new Employee (HR domain).
    """

    key = "employees.create"        # ✅ ENTITY PURE
    domain = "hr"
    permission = "hr.employees.add"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        query format (from frontend):
        {
            user_id: str,
            employee_code?: str,
            full_name: str,
            email?: str,
            phone?: str,
            job_title?: str,
            join_date: "YYYY-MM-DD",
            notes?: str
        }
        """

        # ----------------------------
        # Required fields
        # ----------------------------
        user_id = query.get("user_id")
        full_name = (query.get("full_name") or "").strip()
        join_date = query.get("join_date")

        if not user_id:
            raise ValidationError("User is required")

        if not full_name:
            raise ValidationError("Employee name is required")

        if not join_date:
            raise ValidationError("Join date is required")

        # ----------------------------
        # Validate User
        # ----------------------------
        try:
            employee_user = User.objects.get(
                id=user_id,
                tenant=tenant,
            )
        except User.DoesNotExist:
            raise ValidationError("User not found")

        # ----------------------------
        # Uniqueness (tenant invariant)
        # ----------------------------
        if Employee.objects.filter(
            tenant=tenant,
            user_id=user_id,
        ).exists():
            raise ValidationError(
                "This user is already registered as an employee"
            )

        employee_code = (query.get("employee_code") or "").strip()

        if employee_code:
            if Employee.objects.filter(
                tenant=tenant,
                employee_code=employee_code,
            ).exists():
                raise ValidationError(
                    "Employee code already exists"
                )

        # ----------------------------
        # Optional fields
        # ----------------------------
        email = (query.get("email") or "").strip() or None
        phone = (query.get("phone") or "").strip() or None
        job_title = (query.get("job_title") or "").strip() or None
        notes = (query.get("notes") or "").strip() or None

        # ----------------------------
        # Create
        # ----------------------------
        employee = Employee.objects.create(
            tenant=tenant,
            user_id=employee_user.id,
            employee_code=employee_code or None,
            full_name=full_name,
            email=email,
            phone=phone,
            job_title=job_title,
            join_date=join_date,
            notes=notes,
            created_by=user,
        )

        return {
            "id": str(employee.id),
            "message": "Employee created successfully",
        }
