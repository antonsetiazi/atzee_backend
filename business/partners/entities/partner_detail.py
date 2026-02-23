# business/partners/entities/partner_detail.py

from typing import Optional
from django.db.models import Q
from core.entities.contracts import BaseEntity
from business.partners.models import Partner
from core.files.models import File


class PartnerDetailEntity(BaseEntity):
    """
    partners.detail entity

    Menyediakan detail lengkap untuk halaman partner/ustadz:
    - Profil
    - Foto
    - Skills / bidang keahlian
    - Tarif & rating
    - Jadwal tersedia
    """

    key = "partners.detail"
    domain = "business"
    permission = "business.partners.view"

    def query(self, *, user, tenant, query: dict) -> Optional[dict]:
        """
        query: {
            id: str | int
        }
        """
        partner_id = query.get("id")
        if not partner_id:
            return None

        try:
            partner = Partner.objects.get(id=partner_id, tenant=tenant, is_deleted=False)
        except Partner.DoesNotExist:
            return None

        # ambil meta
        meta = partner.meta or {}

        # ambil foto dari File
        images = File.objects.filter(
            entity_type="partners",
            entity_id=partner.id,
            is_deleted=False,
        )

        foto_urls = [img.get_full_url() for img in images]

        # ambil skills
        skills = meta.get("skills", [])

        # ambil jadwal (sementara dummy, nanti bisa dari tabel jadwal booking)
        available_schedule = meta.get("available_schedule", [])

        # serialize response
        data = {
            "id": str(partner.id),
            "name": partner.name,
            "phone": partner.phone,
            "email": partner.email,
            "address": partner.address,
            "notes": partner.notes,
            "base_price": meta.get("base_price"),
            "rating_avg": meta.get("rating_avg"),
            "rating_count": meta.get("rating_count"),
            "skills": skills,
            "available_schedule": "\n".join(available_schedule) if available_schedule else None,
            "foto": foto_urls,
        }

        return data