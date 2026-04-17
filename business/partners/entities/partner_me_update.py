# business/partners/entities/partner_me_update.py

from business.partners import selectors
from core.entities.contracts import BaseEntity
from business.enum.permissions import BusinessPermission


class PartnerMeUpdateEntity(BaseEntity):
    key = "partners.me.update"
    domain = "business"
    permission = BusinessPermission.PARTNERS_PORTAL_UPDATE

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:
        partner = selectors.get_my_partner(
            tenant=tenant,
            user=user,
        )

        if not partner:
            raise Exception("Partner profile not found")

        # ======================================
        # BASIC FIELDS
        # ======================================
        partner.name = data.get("name", partner.name)
        partner.email = data.get("email", partner.email)
        partner.phone = data.get("phone", partner.phone)
        partner.address = data.get("address", partner.address)

        # ======================================
        # META FIELDS
        # ======================================
        meta = partner.meta or {}

        meta["specialization"] = data.get(
            "specialization",
            meta.get("specialization"),
        )

        meta["bio"] = data.get(
            "bio",
            meta.get("bio"),
        )

        meta["working_hours_label"] = data.get(
            "working_hours_label",
            meta.get("working_hours_label"),
        )

        partner.meta = meta
        partner.updated_by = user
        partner.save()

        return {
            "success": True,
            "message": "Profile updated successfully",
            "id": str(partner.id),
        }