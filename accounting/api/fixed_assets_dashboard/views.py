# accounting/api/fixed_assets_dashboard/views.py

from django.db import models
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import AssetCategory, DepreciationEntry, FixedAsset
from core.tenants.services import TenantService


# =========================================================
# 1. DASHBOARD SUMMARY
# =========================================================
class FixedAssetDashboardSummaryAPIView(APIView):

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        qs = FixedAsset.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        data = qs.aggregate(
            total_assets=Count("id"),
            active_assets=Count("id", filter=models.Q(status="active")),
            disposed_assets=Count("id", filter=models.Q(status="disposed")),
            total_acquisition_value=Sum("purchase_cost"),
            total_book_value=Sum("book_value"),
            total_accumulated_depreciation=Sum("accumulated_depreciation"),
        )

        return Response(data)


# =========================================================
# 2. CATEGORY SUMMARY
# =========================================================
class AssetCategorySummaryAPIView(APIView):

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        qs = AssetCategory.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).annotate(
            asset_count=Count("assets"),
            acquisition_value=Sum("assets__purchase_cost"),
            book_value=Sum("assets__book_value"),
        )

        return Response(
            [
                {
                    "category_name": c.name,
                    "asset_count": c.asset_count or 0,
                    "acquisition_value": c.acquisition_value or 0,
                    "book_value": c.book_value or 0,
                }
                for c in qs
            ]
        )


# =========================================================
# 3. MONTHLY DEPRECIATION SUMMARY
# =========================================================
class MonthlyDepreciationSummaryAPIView(APIView):

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        qs = (
            DepreciationEntry.objects.filter(
                tenant=tenant,
                is_deleted=False,
            )
            .annotate(
                period=TruncMonth("period_date"),
            )
            .values("period")
            .annotate(
                depreciation_amount=Sum("depreciation_amount"),
            )
            .order_by("period")
        )

        return Response(
            [
                {
                    "period": x["period"].strftime("%Y-%m"),
                    "depreciation_amount": x["depreciation_amount"] or 0,
                }
                for x in qs
            ]
        )
