# business/customers/entities/customer_create.py

from core.entities.contracts import BaseEntity
from business.customers.models import Customer
from django.core.exceptions import ValidationError


class CustomerCreateEntity(BaseEntity):
    """
    customers.create entity
    """

    key = "customers.create"
    domain = "business"
    permission = "business.customers.add"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        query format (from frontend):
        {
            code?: str,
            name: str,
            phone?: str,
            email?: str,
            address?: str,
            notes?: str
        }
        """

        name = (query.get("name") or "").strip()
        if not name:
            raise ValidationError("Customer name is required")

        code = (query.get("code") or "").strip() or None

        # 🔒 unique per tenant (optional code)
        if code:
            if Customer.objects.filter(tenant=tenant, code=code).exists():
                raise ValidationError("Customer code already exists")

        customer = Customer.objects.create(
            tenant=tenant,
            code=code,
            name=name,
            phone=query.get("phone"),
            email=query.get("email"),
            address=query.get("address"),
            notes=query.get("notes"),
            created_by=user,
        )

        return {
            "id": str(customer.id),
            "message": "Customer created successfully",
        }
