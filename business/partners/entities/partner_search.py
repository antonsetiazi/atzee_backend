# business/partners/entities/partner_search.py

import math
from django.db.models import Q
from core.entities.contracts import BaseEntity
from business.partners.models import Partner
from core.files.selectors import get_files_by_relations
from django.conf import settings

base_url = settings.BASE_BACKEND_URL

class PartnerSearchEntity(BaseEntity):
    """
    partners.search entity

    Advanced search with:
    - location radius
    - skill filter
    - price range
    - rating filter
    - sorting
    """

    key = "partners.search"
    domain = "business"
    permission = "business.partners.view"

    EARTH_RADIUS_KM = 6371

    def _haversine(self, lat1, lng1, lat2, lng2):
        """
        Calculate distance between two lat/lng points in KM.
        """
        lat1, lng1, lat2, lng2 = map(
            math.radians, [lat1, lng1, lat2, lng2]
        )

        dlat = lat2 - lat1
        dlng = lng2 - lng1

        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1)
            * math.cos(lat2)
            * math.sin(dlng / 2) ** 2
        )

        c = 2 * math.asin(math.sqrt(a))

        return self.EARTH_RADIUS_KM * c

    def query(self, *, user, tenant, query: dict, request=None) -> dict:
        """
        Expected query format:

        {
            lat?: float,
            lng?: float,
            radius_km?: float,
            skills?: list[str],
            min_price?: number,
            max_price?: number,
            min_rating?: number,
            sort_by?: "nearest" | "rating" | "cheapest",
            page?: int,
            pageSize?: int
        }
        """

        qs = Partner.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        # --- BASIC FILTERS ---
        skills = query.get("skills") or []
        min_price = query.get("min_price")
        max_price = query.get("max_price")
        min_rating = query.get("min_rating")

        if skills:
            skill_query = Q()
            for skill in skills:
                skill_query |= Q(meta__skills__icontains=skill)
            qs = qs.filter(skill_query)

        if min_price is not None:
            qs = qs.filter(meta__base_price__gte=min_price)

        if max_price is not None:
            qs = qs.filter(meta__base_price__lte=max_price)

        if min_rating is not None:
            qs = qs.filter(meta__rating_avg__gte=min_rating)

        # --- LOCATION FILTER ---
        lat = query.get("lat")
        lng = query.get("lng")
        radius_km = query.get("radius_km")

        results = []
        for partner in qs:
            meta = partner.meta or {}

            p_lat = meta.get("lat")
            p_lng = meta.get("lng")

            distance = None

            if lat and lng and p_lat and p_lng:
                distance = self._haversine(
                    float(lat),
                    float(lng),
                    float(p_lat),
                    float(p_lng),
                )

                if radius_km and distance > float(radius_km):
                    continue

            results.append((partner, distance))

        # --- SORTING ---
        sort_by = query.get("sort_by")

        if sort_by == "nearest":
            results.sort(key=lambda x: x[1] or 999999)

        elif sort_by == "rating":
            results.sort(
                key=lambda x: x[0].meta.get("rating_avg", 0),
                reverse=True,
            )

        elif sort_by == "cheapest":
            results.sort(
                key=lambda x: x[0].meta.get("base_price", 0)
            )

        # Default sort: rating desc
        else:
            results.sort(
                key=lambda x: x[0].meta.get("rating_avg", 0),
                reverse=True,
            )

        # --- PAGINATION ---
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        sliced = results[offset:limit]


        partner_ids = [str(partner.id) for partner, _ in sliced]

        files = get_files_by_relations(
            tenant=tenant,
            related_entity="partner_image",
            related_ids=partner_ids,
        )

        image_map = {}

        for f in files:
            if f.related_id not in image_map:
                image_map[f.related_id] = f.get_download_url(request=request)
                

        # --- SERIALIZE ---
        data = []
        for partner, distance in sliced:
            meta = partner.meta or {}

            data.append(
                {
                    "id": str(partner.id),
                    "name": partner.name,
                    "phone": partner.phone,
                    "email": partner.email,
                    "base_price": float(partner.base_price) if partner.base_price is not None else None,
                    "rating_avg": float(partner.rating_avg) if partner.rating_avg is not None else None,
                    "rating_count": partner.rating_count,
                    "skills": meta.get("skills", []),  # kalau skill masih di meta
                    "distance_km": round(distance, 2) if distance else None,
                    "image_url": f"{base_url}{image_map.get(str(partner.id))  or '/static/default-avatar.jpg'}",
                }
            )

        return {
            "items": data,
            "total": len(results),
        }