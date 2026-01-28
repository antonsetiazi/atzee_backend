# business/customers/entities/customer_edit.py

from core.entities.contracts import BaseEntity
from business.customers.models import Customer
from django.core.exceptions import ValidationError


class CustomerEditEntity(BaseEntity):
    """
    customers.edit entity
    """

    key = "customers.edit"
    permission = "business.customers.update"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        query format (from frontend):
        {
            id: str,
            code?: str,
            name?: str,
            phone?: str,
            email?: str,
            address?: str,
            notes?: str
        }
        """

        customer_id = query.get("id")
        if not customer_id:
            raise ValidationError("Customer ID is required")

        # ambil customer
        try:
            customer = Customer.objects.get(id=customer_id, tenant=tenant)
        except Customer.DoesNotExist:
            raise ValidationError("Customer not found")

        # ambil data update
        name = (query.get("name") or "").strip()
        code = (query.get("code") or "").strip() or None
        phone = query.get("phone")
        email = query.get("email")
        address = query.get("address")
        notes = query.get("notes")

        if name:
            customer.name = name

        if code:
            # cek unique code per tenant kecuali customer ini sendiri
            if Customer.objects.filter(tenant=tenant, code=code).exclude(id=customer.id).exists():
                raise ValidationError("Customer code already exists")
            customer.code = code

        if phone is not None:
            customer.phone = phone
        if email is not None:
            customer.email = email
        if address is not None:
            customer.address = address
        if notes is not None:
            customer.notes = notes

        customer.updated_by = user
        customer.save(update_fields=[
            "name",
            "code",
            "phone",
            "email",
            "address",
            "notes",
            "updated_by",
            "updated_at",
        ])

        return {
            "id": str(customer.id),
            "message": "Customer updated successfully",
        }
