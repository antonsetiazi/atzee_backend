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

        
        # =====================================
        # WORKING HOURS
        # =====================================
        working_hours = self._working_hours_raw(service)

        return {
            "id": str(partner.id),
            "name": partner.name,
            "email": partner.email or "-",
            "phone": partner.phone or "-",
            "address": partner.address or "-",

            "location_label": partner.location_label,

            "country_id": partner.country_id,
            "region_id": partner.region_id,
            "city_id": partner.city_id,

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

            # 🔥 for display page
            "working_hours_label": self._working_hours_label(working_hours),

            # 🔥 for edit form
            "working_hours": working_hours,

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

    # ==========================================
    # RAW STRUCTURED VALUE
    # ==========================================
    def _working_hours_raw(self, service):
        if not service:
            return {
                "start": 8,
                "end": 17,
            }

        wh = service.working_hours or {}

        return {
            "start": int(wh.get("start", 8)),
            "end": int(wh.get("end", 17)),
        }
    
    # ==========================================
    # LABEL FOR UI DISPLAY
    # ==========================================
    def _working_hours_label(self, wh):
        start = wh.get("start")
        end = wh.get("end")

        return f"{start}:00 - {end}:00"