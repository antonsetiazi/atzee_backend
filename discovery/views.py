# discovery/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from core.tenants.services import TenantService
from discovery.selectors import get_product_listings, get_service_listings
from discovery.serializers.product_listing_serializer import ProductListingSerializer
from discovery.serializers.service_listing_serializer import ServiceListingSerializer
from discovery.selectors import get_service_detail
from discovery.serializers.service_detail_serializer import ServiceDetailSerializer
from rest_framework import status


class ProductListingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)
        search = request.GET.get("search")

        qs = get_product_listings(
            tenant=tenant,
            search=search,
        )

        page = int(request.GET.get("page", 1))
        per_page = 12

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
            "meta": {
                "page": page,
                "per_page": per_page,
                "total": total,
            }
        })
    

class ServiceListingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)
        search = request.GET.get("search")
        
        qs = get_service_listings(
            tenant=tenant,
            search=search,
        )

        page = int(request.GET.get("page", 1))
        per_page = 12

        start = (page - 1) * per_page
        end = start + per_page

        total = qs.count()

        serializer = ServiceListingSerializer(
            qs[start:end], 
            many=True, 
            context={
                "request": request,
                "tenant": tenant,
            },
        )

        return Response({
            "data": serializer.data,
            "meta": {
                "page": page,
                "per_page": per_page,
                "total": total,
            }
        })    
    

class ServiceDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, partner_id):
        tenant = TenantService.get_current_tenant(request)

        data = get_service_detail(
            tenant=tenant,
            partner_id=partner_id,
        )

        if not data:
            return Response(
                {"detail": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ServiceDetailSerializer(
            data,
            context={"request": request},
        )

        return Response(serializer.data)    