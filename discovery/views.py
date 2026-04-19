# discovery/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from core.tenants.services import TenantService
from discovery.services.listing_service import get_service_listings
from discovery.serializers.product_listing_serializer import ProductListingSerializer
from discovery.serializers.service_listing_serializer import ServiceListingSerializer
from discovery.serializers.service_detail_serializer import ServiceDetailSerializer
from rest_framework import status
from discovery.selectors import marketplace as marketplace_selector
from core.classifications.categories import selectors as category_selectors
from core.geo.cities.models import City

import math

class CategoryListView(APIView):
    """
    List categories by scope (public endpoint, no auth required)
    GET /discovery/categories/?scope=partners.service
    """
    permission_classes = [AllowAny]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)
        scope = request.GET.get("scope")
        if not scope:
            return Response({"detail": "scope parameter required"}, status=400)

        qs = category_selectors.get_category_queryset(tenant=tenant)
        qs = qs.filter(scope=scope).order_by("name")

        categories = [
            {
                "id": c.id,
                "code": c.code,
                "name": c.name,
                "scope": c.scope,
                "parent": c.parent_id,
            }
            for c in qs
        ]

        return Response(categories)
    
class ProductListingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)
        search = request.GET.get("search")
        page = int(request.GET.get("page", 1))
        per_page = 12

        qs = marketplace_selector.get_product_listings(
            tenant=tenant,
            search=search,
        )

        start = (page - 1) * per_page
        end = start + per_page
        total = qs.count()

        serializer = ProductListingSerializer(
            qs[start:end],
            many=True,
            context={"request": request},
        )

        return Response({
            "data": serializer.data,
            "meta": {"page": page, "per_page": per_page, "total": total},
        })


class ServiceListingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            tenant = TenantService.get_current_tenant(request)

            search = request.GET.get("search")
            source = request.GET.get("source", "marketplace") 
            categories = request.GET.getlist("category")
            lat = request.GET.get("lat")
            lng = request.GET.get("lng")
            radius = request.GET.get("radius")
            city = request.GET.get("city")
            sort = request.GET.get("sort", "latest")

            lat = float(lat) if lat else None
            lng = float(lng) if lng else None
            radius = int(radius) if radius else None

            qs = get_service_listings(
                tenant=tenant,
                search=search,
                source=source,
                categories=categories,
                city=city,
                lat=lat,
                lng=lng,
                radius_km=radius,
                sort=sort,
            )

            page = int(request.GET.get("page", 1))
            per_page = 12

            start = (page - 1) * per_page
            end = start + per_page

            total = len(qs)

            serializer = ServiceListingSerializer(
                qs[start:end],
                many=True,
                context={
                    "request": request,
                    "tenant": tenant,
                },
            )

            total_pages = math.ceil(total / per_page)

            return Response({
                "data": serializer.data,
                "meta": {
                    "page": page,
                    "per_page": per_page,
                    "total": total,
                    "total_pages": total_pages,
                }
            })
        except Exception as e:
            print(e)

class ServiceDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, partner_id):
        tenant = TenantService.get_current_tenant(request)

        data = marketplace_selector.get_service_detail(
            tenant=tenant,
            partner_id=partner_id,
        )

        if not data:
            return Response({"detail": "Not found"}, status=404)

        serializer = ServiceDetailSerializer(
            data,
            context={"request": request},
        )

        return Response(serializer.data)
    

class CityListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        cities = City.objects.all().order_by("name")

        data = [
            {
                "id": c.id,
                "code": c.code,
                "name": c.name,
            }
            for c in cities
        ]

        return Response(data)    