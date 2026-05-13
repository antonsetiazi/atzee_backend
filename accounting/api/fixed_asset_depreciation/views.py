# accounting/api/fixed_asset_depreciation/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import DepreciationEntry
from accounting.services.depreciation_batch_service import (
    DepreciationBatchService,
)
from core.tenants.services import (
    TenantService,
)

from .serializers import (
    FixedAssetDepreciationRunSerializer,
)


class FixedAssetBulkDepreciationAPIView(APIView):
    def post(self, request):
        try:
            tenant = TenantService.get_current_tenant(request)
            serializer = FixedAssetDepreciationRunSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            result = DepreciationBatchService.run_monthly_depreciation(
                tenant=tenant,
                user=request.user,
                period_date=(serializer.validated_data["period_date"]),
            )

            return Response(
                result,
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class FixedAssetDepreciationListAPIView(APIView):
    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        qs = (
            DepreciationEntry.objects.filter(
                tenant=tenant,
                is_deleted=False,
            )
            .select_related("asset")
            .order_by("-period_date")
        )

        return Response(
            [
                {
                    "id": str(x.id),
                    "asset_id": str(x.asset.id),
                    "asset_name": x.asset.name,
                    "asset_number": (x.asset.asset_number),
                    # UI CONTRACT
                    "period": x.period_date,
                    "depreciation_date": (x.created_at),
                    "depreciation_amount": (x.depreciation_amount),
                    "accumulated_depreciation": (x.accumulated_depreciation),
                    "book_value": (x.book_value_after),
                    "journal_id": (str(x.journal.id) if x.journal else None),
                    "posted_at": (x.updated_at),
                    "created_at": (x.created_at),
                }
                for x in qs
            ]
        )
