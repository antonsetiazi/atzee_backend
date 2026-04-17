# business/partners/entities/partner_me.py

from core.entities.contracts import BaseEntity
from business.partners.models import Partner
from business.enum.permissions import BusinessPermission
from core.files.models import File
from django.conf import settings

class PartnerMeEntity(BaseEntity):
    key = "partners.me"
    domain = "business"
    permission = BusinessPermission.PARTNERS_PORTAL

    def query(self, *, user, tenant, query: dict) -> dict:
        partner = (
            Partner.objects
            .filter(
                tenant=tenant,
                core_user=user,
                is_deleted=False,
            )
            .select_related(
                "city",
                "region",
            )
            .first()
        )

        if not partner:
            return {
                "items": [],
                "empty": True,
                "message": "Partner profile not found."
            }

        service = getattr(partner, "service_profile", None)

        # 🔥 ambil images partner
        files = File.objects.filter(
            tenant=tenant,
            related_entity="partner_image",
            related_id=str(partner.id),
            is_deleted=False,
        ).order_by("-created_at")

        image_urls = []
        
        for f in files:
            image_urls.append(
                f"{settings.BASE_BACKEND_URL}/api/files/{f.id}/download/"
            )

        return {
            "id": str(partner.id),
            "name": partner.name,
            "email": partner.email or "-",
            "phone": partner.phone or "-",
            "address": partner.address or "-",

            "location_label": partner.location_label,

            "rating_avg": float(partner.rating_avg or 0),
            "rating_count": int(partner.rating_count or 0),

            "specialization": (
                service.specialization
                if service and service.specialization
                else "-"
            ),

            "bio": (
                service.bio
                if service and service.bio
                else "No biography yet."
            ),

            "working_hours_label": self._working_hours(service),

            # temp stat dummy (nanti real query)
            "total_bookings": 0,
            "completed_orders": 0,

            "status_label": (
                "Active"
                if partner.meta.get("is_active", True)
                else "Inactive"
            ),

            # image placeholder
            "image_urls": image_urls,
        }

    def _working_hours(self, service):
        if not service:
            return "-"

        wh = service.working_hours or {}

        start = wh.get("start")
        end = wh.get("end")

        if start is None or end is None:
            return "-"

        return f"{start}:00 - {end}:00"