# business/partners/entities/partner_create.py

from core.entities.contracts import BaseEntity
from business.partners.models import Partner
from django.core.exceptions import ValidationError


class PartnerCreateEntity(BaseEntity):
    """
    partners.create entity
    """

    key = "partners.create"
    domain = "business"
    permission = "business.partners.add"

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
            raise ValidationError("Partner name is required")

        code = (query.get("code") or "").strip() or None

        # 🔒 unique per tenant (optional code)
        if code:
            if Partner.objects.filter(tenant=tenant, code=code).exists():
                raise ValidationError("Partner code already exists")

        partner = Partner.objects.create(
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
            "id": str(partner.id),
            "message": "Partner created successfully",
        }
