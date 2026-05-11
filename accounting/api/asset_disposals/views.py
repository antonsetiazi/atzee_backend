# accounting/api/asset_disposals/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import (
    AssetDisposal,
)
from accounting.services.asset_disposal_service import (
    AssetDisposalService,
)
from core.tenants.services import (
    TenantService,
)

from .serializers import (
    AssetDisposalCreateSerializer,
    AssetDisposalReadSerializer,
)


class AssetDisposalListAPIView(APIView):

    def get(self, request):

        tenant = TenantService.get_current_tenant(request)

        qs = AssetDisposal.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).select_related("asset")

        qs = qs.order_by(
            "-disposal_date",
            "-created_at",
        )

        data = AssetDisposalReadSerializer(
            qs,
            many=True,
        ).data

        return Response(data)


class AssetDisposalCreateAPIView(APIView):

    def post(self, request):

        try:

            tenant = TenantService.get_current_tenant(request)

            serializer = AssetDisposalCreateSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            disposal = AssetDisposalService.dispose_asset(
                tenant=tenant,
                user=request.user,
                asset_id=(serializer.validated_data["asset_id"]),
                disposal_date=(serializer.validated_data["disposal_date"]),
                disposal_value=(serializer.validated_data["disposal_value"]),
                notes=(
                    serializer.validated_data.get(
                        "notes",
                        "",
                    )
                ),
            )

            data = AssetDisposalReadSerializer(disposal).data

            return Response(
                data,
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:

            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class AssetDisposalDetailAPIView(APIView):

    def get(self, request, disposal_id):

        try:

            tenant = TenantService.get_current_tenant(request)

            disposal = AssetDisposal.objects.select_related("asset").get(
                id=disposal_id,
                tenant=tenant,
                is_deleted=False,
            )

            data = AssetDisposalReadSerializer(disposal).data

            return Response(data)

        except AssetDisposal.DoesNotExist:

            return Response(
                {"error": "Disposal not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
