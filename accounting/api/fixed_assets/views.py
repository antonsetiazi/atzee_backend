# accounting/api/fixed_assets/views.py

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import FixedAsset
from accounting.services.depreciation_service import (
    DepreciationService,
)
from accounting.services.fixed_asset_service import (
    FixedAssetService,
)
from core.tenants.services import TenantService

from .serializers import (
    FixedAssetCreateSerializer,
    FixedAssetReadSerializer,
)


class FixedAssetListAPIView(APIView):

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)
        qs = FixedAsset.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        search = request.GET.get("search")

        if search:
            qs = qs.filter(name__icontains=search)

        status_filter = request.GET.get("status")

        if status_filter:
            qs = qs.filter(status=status_filter)

        qs = qs.order_by(
            "-capitalization_date",
            "asset_number",
        )

        data = FixedAssetReadSerializer(
            qs,
            many=True,
        ).data

        return Response(data)


class FixedAssetCreateAPIView(APIView):

    def post(self, request):

        try:
            tenant = TenantService.get_current_tenant(request)
            serializer = FixedAssetCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            asset = FixedAssetService.create_asset(
                tenant=tenant,
                user=request.user,
                asset_number=(serializer.validated_data["asset_number"]),
                name=(serializer.validated_data["name"]),
                description=(
                    serializer.validated_data.get(
                        "description",
                        "",
                    )
                ),
                serial_number=serializer.validated_data.get(
                    "serial_number", ""
                ),
                location=serializer.validated_data.get("location", ""),
                category_id=(serializer.validated_data["category_id"]),
                purchase_date=(serializer.validated_data["purchase_date"]),
                capitalization_date=(
                    serializer.validated_data["capitalization_date"]
                ),
                purchase_cost=(serializer.validated_data["purchase_cost"]),
                depreciation_start_date=(
                    serializer.validated_data["depreciation_start_date"]
                ),
                salvage_value=(serializer.validated_data.get("salvage_value")),
            )

            data = FixedAssetReadSerializer(asset).data

            return Response(
                data,
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class FixedAssetDetailAPIView(APIView):

    def get(self, request, asset_id):

        try:

            tenant = TenantService.get_current_tenant(request)

            asset = FixedAsset.objects.get(
                id=asset_id,
                tenant=tenant,
                is_deleted=False,
            )

            data = FixedAssetReadSerializer(asset).data

            return Response(data)

        except FixedAsset.DoesNotExist:
            return Response(
                {"error": "Asset not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class FixedAssetActivateAPIView(APIView):

    def post(self, request, asset_id):

        tenant = TenantService.get_current_tenant(request)

        asset = get_object_or_404(
            FixedAsset,
            id=asset_id,
            tenant=tenant,
            is_deleted=False,
        )

        try:

            asset = FixedAssetService.activate_asset(
                asset=asset,
                user=request.user,
            )

            data = FixedAssetReadSerializer(asset).data

            return Response(data)

        except Exception as e:

            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class FixedAssetDepreciateAPIView(APIView):

    def post(self, request, asset_id):
        tenant = TenantService.get_current_tenant(request)
        asset = get_object_or_404(
            FixedAsset,
            id=asset_id,
            tenant=tenant,
            is_deleted=False,
        )

        try:
            period_date = request.data.get("period_date")
            entry = DepreciationService.run_asset_depreciation(
                asset=asset,
                period_date=period_date,
                user=request.user,
            )

            return Response(
                {
                    "success": True,
                    "entry_id": str(entry.id),
                }
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class FixedAssetUpdateAPIView(APIView):

    def put(self, request, asset_id):
        tenant = TenantService.get_current_tenant(request)
        asset = get_object_or_404(
            FixedAsset,
            id=asset_id,
            tenant=tenant,
            is_deleted=False,
        )

        serializer = FixedAssetCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        asset = FixedAssetService.update_asset(
            asset=asset,
            user=request.user,
            data=serializer.validated_data,
        )

        return Response(FixedAssetReadSerializer(asset).data)
