# business/partners/entities/partner_me_update.py

from business.partners import selectors
from business.partners.models.service_profile import PartnerServiceProfile
from core.entities.contracts import BaseEntity
from business.enum.permissions import BusinessPermission
from core.geo.countries.models import Country
from core.geo.regions.models import Region
from core.geo.cities.models import City


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
        # BASIC PARTNER
        # ======================================
        partner.name = data.get("name", partner.name)
        partner.email = data.get("email", partner.email)
        partner.phone = data.get("phone", partner.phone)
        partner.address = data.get("address", partner.address)

        country_id = data.get("country_id")
        region_id = data.get("region_id")
        city_id = data.get("city_id")

        partner.country_id = country_id or None
        partner.region_id = region_id or None
        partner.city_id = city_id or None

        partner.updated_by = user
        partner.save()

        # ======================================
        # SERVICE PROFILE
        # ======================================
        profile, _ = PartnerServiceProfile.objects.get_or_create(
            partner=partner
        )

        profile.specialization = data.get(
            "specialization",
            profile.specialization
        )

        profile.bio = data.get(
            "bio",
            profile.bio
        )

        working_hours = data.get("working_hours") or {}

        profile.working_hours = {
            "start": int(working_hours.get("start", 8)),
            "end": int(working_hours.get("end", 17)),
        }

        profile.save()

        return {
            "success": True,
            "message": "Profile updated successfully",
            "id": str(partner.id),
        }